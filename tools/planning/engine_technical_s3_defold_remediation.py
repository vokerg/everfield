#!/usr/bin/env python3
'''W2-ENG-TECH-S3-01 bounded Defold S3 archive/bundle remediation.'''
from __future__ import annotations
import argparse, importlib.util, json, pathlib, shutil, stat, tempfile

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    if not s or not s.loader: raise RuntimeError(f'{name} module unavailable')
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--evidence',required=True)
    ap.add_argument('--artifact-lock',required=True)
    ap.add_argument('--runner',default='tools/planning/engine_technical_s3_probe.py')
    ap.add_argument('--capability-probe',default='tools/planning/engine_toolchain_probe.py')
    args=ap.parse_args()
    runner=load(pathlib.Path(args.runner),'s3runner')
    cap=load(pathlib.Path(args.capability_probe),'cap')
    ep=pathlib.Path(args.evidence); evidence=json.loads(ep.read_text())
    prior=evidence['results']['Defold']
    lock=cap.load_artifact_lock(pathlib.Path(args.artifact_lock))
    with tempfile.TemporaryDirectory(prefix='everfield-s3-defold-rem-') as td:
        root=pathlib.Path(td); tool=cap.probe_defold(root,lock)
        jar=root/'bob-1.13.0.jar'; java=(tool.get('java') or {}).get('path') or shutil.which('java')
        result={'candidate':'Defold','scenario':'S3','toolchain':tool,'producer_disposition':'INCONCLUSIVE_HARNESS_OR_INFRA','review_required_before_trust':True}
        if tool.get('status')=='CAPABLE' and jar.exists() and java:
            p=root/'defold-s3'; p.mkdir(); (p/'input').mkdir(); (p/'input/game.input_binding').write_text('')
            (p/'game.project').write_text('[project]\ntitle = EverfieldS3\n[bootstrap]\nmain_collection = /main.collectionc\n[display]\nwidth = 320\nheight = 180\n')
            (p/'main.collection').write_text('name: "main"\nscale_along_z: 0\nembedded_instances {\n id: "controller"\n data: "components {\\n  id: \\"script\\"\\n  component: \\"/controller.script\\"\\n}\\n"\n}\n')
            (p/'controller.script').write_text(runner.LUA)
            builds=[]; bundle=None; variant=None
            for v in ('headless','debug'):
                bdir=p/f'bundle-{v}'
                r=runner.run([java,'-jar',str(jar),'--root',str(p),'--bundle-output',str(bdir),'--variant',v,'--platform','x86_64-linux','--archive','resolve','build','bundle'],cwd=p,timeout=900)
                builds.append({'variant':v,'archive_enabled':True,'command':r})
                if runner.ok(r): bundle=bdir; variant=v; break
            exe=runner.bundle_exe(bundle)
            attempts=[]
            if bundle and exe:
                for name,pert in (('N1',False),('N2',False),('FI1',True)):
                    ws=root/'runs/defold'/name; shutil.copytree(bundle,ws); x=ws/exe.relative_to(bundle)
                    rr=runner.run([str(x)],cwd=x.parent,env={'EVERFIELD_PERTURB':'1' if pert else '0'},timeout=120)
                    if not runner.ok(rr) and shutil.which('xvfb-run'):
                        rr=runner.run(['xvfb-run','-a',str(x)],cwd=x.parent,env={'EVERFIELD_PERTURB':'1' if pert else '0'},timeout=120)
                    attempts.append(runner.record('Defold',name,pert,ws,rr))
                result=runner.summary('Defold',tool,attempts,builds)
                result['bundle_variant']=variant; result['bundle_executable_sha256']=runner.digest_file(exe)
            else:
                result=runner.summary('Defold',tool,[],builds); result['bundle_variant']=variant
        evidence.setdefault('producer_remediation_history',[]).append({'candidate':'Defold','reason':'bob_bundle_required_archive_generation','prior_result':prior})
        evidence['results']['Defold']=result
        good=[k for k,v in evidence['results'].items() if v.get('producer_disposition')=='PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW']
        evidence['provisional_review_pending_s3_pass_candidates']=good
        evidence['provisional_review_pending_s3_pass_count']=len(good)
        evidence['defold_archive_remediation_applied']=True
        ep.write_text(json.dumps(evidence,sort_keys=True,indent=2)+'\n')
        print(json.dumps({'defold':result.get('producer_disposition'),'pass_candidates':good},sort_keys=True))
    return 0
if __name__=='__main__': raise SystemExit(main())
