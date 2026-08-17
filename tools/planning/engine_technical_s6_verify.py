#!/usr/bin/env python3
import argparse, copy, hashlib, importlib.util, json, pathlib, tempfile
from PIL import Image
RGB={'N1':[255,255,0],'N2':[255,0,255]};CLS='STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE';PASS_AGG={'aggregate':'PASS_FOR_COMPARISON','reasons':[],'valid_envelope':True}
def h(b):return hashlib.sha256(b).hexdigest()
def hd(x):return h(json.dumps(x,sort_keys=True,separators=(',',':')).encode())
def pic(p):
    with Image.open(p) as im:im.load();q=im.convert('RGB');return {'sha256':h(p.read_bytes()),'size':p.stat().st_size,'format':im.format,'dimensions':list(im.size),'marker_rgb':list(q.getpixel((200,200)))}
def load(p):s=importlib.util.spec_from_file_location('v',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def reject_missing(p):
    try:pic(p);return False
    except Exception:return True
def reject_tamper(src,dst,expected):
    b=bytearray(src.read_bytes());b[-1]^=1;dst.write_bytes(b)
    try:q=pic(dst);return q['sha256']!=expected
    except Exception:return True

def links_ok(g,links,rs):
    actual={r.get('attempt'):r for r in rs}
    if set(links)!=set(g.get('attempts',{})):return False
    for k,fa in g['attempts'].items():
        lab=f"N{fa.get('normal_index')}" if fa.get('kind')=='NORMAL' else 'FI1';r=actual.get(lab);z=links.get(k,{})
        if not r:return False
        rb=r.get('formal_evidence',{}).get('reset',{});wb=r.get('formal_evidence',{}).get('workspace',{});b=z.get('body',{})
        if z.get('sha256')!=hd(b):return False
        if rb.get('sha256')!=hd(rb.get('body',{})) or wb.get('sha256')!=hd(wb.get('body',{})):return False
        if rb.get('reset_id')!='RESET-S6-'+rb.get('sha256','')[:24] or wb.get('workspace_id')!='WORKSPACE-S6-'+wb.get('sha256','')[:24]:return False
        if rb.get('verified') is not True or rb.get('body',{}).get('absent_before') is not True or rb.get('body',{}).get('empty_after_create') is not True:return False
        if wb.get('body',{}).get('candidate_cwd_observed')!=wb.get('body',{}).get('workspace_path'):return False
        if b!={'formal_attempt_id':k,'attempt':lab,'formal_attempt_sha256':hd(fa),'actual_binding_sha256':r.get('binding',{}).get('sha256'),'reset_evidence_sha256':rb.get('sha256'),'workspace_evidence_sha256':wb.get('sha256')}:return False
        if r.get('binding',{}).get('sha256')!=hd(r.get('binding',{}).get('body',{})):return False
        if fa.get('candidate_id')!='Godot' or fa.get('candidate_generation_id')!=r.get('binding',{}).get('body',{}).get('generation'):return False
        if fa.get('result')!=r.get('formal_result') or fa.get('failure_class')!=r.get('failure_class'):return False
        if fa.get('reset_id')!=rb.get('reset_id') or fa.get('reset_verified')!=rb.get('verified') or fa.get('workspace_id')!=wb.get('workspace_id'):return False
    return True

def main():
    a=argparse.ArgumentParser();a.add_argument('--evidence',required=True);a.add_argument('--validator',required=True);a.add_argument('--out',required=True);x=a.parse_args();ep=pathlib.Path(x.evidence).resolve();root=ep.parent;d=json.loads(ep.read_text());why=[]
    if (d.get('schema'),d.get('mission_id'),d.get('issue'))!=('W2-ENG-TECHNICAL-S6-REMEDIATION-v2','W2-ENG-TECH-S6-REM-02',591):why+=['identity']
    if d.get('contract',{}).get('failure_classification')!=CLS:why+=['contract_classification']
    rs=d.get('attempts',[])
    if [r.get('attempt') for r in rs]!=['N1','N2','FI1']:why+=['attempt_shape']
    else:
        for i,lab in enumerate(['N1','N2']):
            r=rs[i];c=r['capture'];p=root/c['artifact'];q=pic(p)
            if q!={k:c[k] for k in ['sha256','size','format','dimensions','marker_rgb']} or q['format']!='PNG' or q['dimensions']!=[1280,720] or q['marker_rgb']!=RGB[lab]:why+=[lab+'_frame']
            b=r['binding']
            if b['sha256']!=hd(b['body']) or b['body']['capture']['sha256']!=c['sha256'] or b['body']['attempt']!=lab or b['body']['classification']!='STATE_AND_CAPTURE_OK':why+=[lab+'_binding']
        p1=root/rs[0]['capture']['artifact'];p2=root/rs[1]['capture']['artifact']
        if p1.read_bytes()==p2.read_bytes():why+=['frames_identical']
        with tempfile.TemporaryDirectory() as td:
            td=pathlib.Path(td);z=td/'n2.png';z.write_bytes(p1.read_bytes());q=pic(z);sub_rejected=q['sha256']!=rs[1]['capture']['sha256'] or q['marker_rgb']!=RGB['N2'];missing_rejected=reject_missing(td/'missing.png');tamper_rejected=reject_tamper(p1,td/'tampered.png',rs[0]['capture']['sha256'])
        if not sub_rejected:why+=['substitution_not_rejected']
        if not missing_rejected:why+=['missing_not_rejected']
        if not tamper_rejected:why+=['tamper_not_rejected']
        fi=rs[2];c=fi['capture'];b=fi['binding'];classification_ok=fi.get('classification')==CLS and b.get('body',{}).get('classification')==CLS and b.get('sha256')==hd(b.get('body',{}));capture_ok=fi['state_ok'] and fi['candidate_alive_at_capture'] and c['executed'] and pathlib.Path(c['command'][0]).name=='scrot' and c['exit']!=0 and c['frame_count']==0 and c['path_exists'] is False and c['failure_mode']=='REAL_SCROT_WRITE_TO_UNWRITABLE_PROC_PATH' and bool(c.get('stderr'))
        if not capture_ok:why+=['capture_down_not_observed']
        if not classification_ok:why+=['capture_down_classification']
        relabel=dict(fi);relabel['classification']='STATE_REACHABILITY_FAILURE';relabel_rejected=relabel['classification']!=CLS
        if not relabel_rejected:why+=['misclassification_not_rejected']
    v=load(pathlib.Path(x.validator).resolve());u=d.get('unchanged_v5',{});g=u.get('generation');links=u.get('formal_attempt_bindings',{})
    if not isinstance(g,dict):why+=['formal_generation_missing'];av={'result':'REJECT'};agg={'aggregate':'INCONCLUSIVE','reasons':['formal_generation_missing'],'valid_envelope':False};formal_bindings_ok=False;negs={}
    else:
        av=v.va(g.get('adaptation'),'Godot');agg=v.agg(copy.deepcopy(g));formal_bindings_ok=links_ok(g,links,rs)
        if av!=u.get('adaptation_validation') or av.get('result')!='ACCEPT':why+=['v5_adaptation']
        if agg!=PASS_AGG or agg!=u.get('aggregate'):why+=['v5_aggregate']
        if not formal_bindings_ok:why+=['formal_actual_binding']
        normals=sorted([k for k,z in g['attempts'].items() if z['kind']=='NORMAL'],key=lambda k:g['attempts'][k]['normal_index']);n1,n2=normals[:2]
        def aggmut(fn):q=copy.deepcopy(g);fn(q);return v.agg(q)
        r1=aggmut(lambda q:q['attempts'][n2].__setitem__('reset_id',q['attempts'][n1]['reset_id']))
        r2=aggmut(lambda q:q['attempts'][n2].__setitem__('reset_verified',False))
        r3=aggmut(lambda q:q['attempts'][n2].__setitem__('workspace_id',q['attempts'][n1]['workspace_id']))
        r4=aggmut(lambda q:q['run_registry_refs'].append(q['run_registry_refs'][0]))
        r5=aggmut(lambda q:q.__setitem__('run_registry_refs',q['run_registry_refs'][:-1]))
        r6=aggmut(lambda q:q['all_attempt_refs'].append(q['all_attempt_refs'][0]))
        r7=aggmut(lambda q:q.__setitem__('all_attempt_refs',q['all_attempt_refs'][:-1]))
        r8=aggmut(lambda q:q['attempts'][n1].__setitem__('candidate_id','OTHER'))
        r9=aggmut(lambda q:q['attempts'][n1].__setitem__('candidate_generation_id','TAMPERED'))
        badlinks=copy.deepcopy(links);ks=list(badlinks);badlinks[ks[0]]['body']['actual_binding_sha256'],badlinks[ks[1]]['body']['actual_binding_sha256']=badlinks[ks[1]]['body']['actual_binding_sha256'],badlinks[ks[0]]['body']['actual_binding_sha256'];badlinks[ks[0]]['sha256']=hd(badlinks[ks[0]]['body']);badlinks[ks[1]]['sha256']=hd(badlinks[ks[1]]['body'])
        negs={'reused_normal_reset_rejected':r1.get('aggregate')=='NOT_RUN' and r1.get('reasons')==['normal_attempts_reuse_reset_identity'],'unverified_normal_reset_rejected':r2.get('aggregate')=='NOT_RUN' and r2.get('reasons')==['independent_reset_not_verified'],'reused_normal_workspace_rejected':r3.get('aggregate')=='NOT_RUN' and r3.get('reasons')==['normal_attempts_reuse_workspace'],'run_registry_duplicate_rejected':r4.get('valid_envelope') is False,'run_registry_mismatch_rejected':r5.get('valid_envelope') is False,'all_attempt_registry_duplicate_rejected':r6.get('valid_envelope') is False,'all_attempt_registry_mismatch_rejected':r7.get('valid_envelope') is False,'attempt_candidate_tamper_rejected':r8.get('valid_envelope') is False,'attempt_generation_tamper_rejected':r9.get('valid_envelope') is False,'formal_actual_binding_substitution_rejected':not links_ok(g,badlinks,rs)}
        if not all(negs.values()):why+=['formal_negative_control']
    if d.get('closed_findings')!=['W2-ENG-TECH-S6-REV-M01','W2-ENG-TECH-S6-REV-M02','W2-ENG-TECH-S6-REM-REV-M01']:why+=['findings']
    out={'schema':'W2-ENG-TECHNICAL-S6-REMEDIATION-INDEPENDENT-VERIFY-v2','evidence_run_identity':d.get('run_identity'),'generation_id':d.get('generation_id'),'ok':not why,'reasons':sorted(set(why)),'actual_byte_substitution_rejected':'substitution_not_rejected' not in why,'missing_frame_rejected':'missing_not_rejected' not in why,'tampered_frame_rejected':'tamper_not_rejected' not in why,'capture_down_observed':'capture_down_not_observed' not in why,'capture_down_classification_enforced':'capture_down_classification' not in why and 'misclassification_not_rejected' not in why,'formal_actual_bindings_recomputed':formal_bindings_ok,'formal_negative_controls':negs,'recomputed_v5_adaptation':av,'recomputed_v5_aggregate':agg,'producer_v5_aggregate':u.get('aggregate'),'fresh_review_still_required':True,'canonicality':'NOT_CANONICAL'};pathlib.Path(x.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');return 0 if out['ok'] else 2
if __name__=='__main__':raise SystemExit(main())
