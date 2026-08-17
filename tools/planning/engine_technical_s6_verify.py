#!/usr/bin/env python3
import argparse,hashlib,importlib.util,json,pathlib,tempfile
from PIL import Image
RGB={'N1':[255,255,0],'N2':[255,0,255]}
def h(b):return hashlib.sha256(b).hexdigest()
def hd(x):return h(json.dumps(x,sort_keys=True,separators=(',',':')).encode())
def pic(p):
 with Image.open(p) as im:im.load();q=im.convert('RGB');return {'sha256':h(p.read_bytes()),'size':p.stat().st_size,'format':im.format,'dimensions':list(im.size),'marker_rgb':list(q.getpixel((200,200)))}
def load(p):s=importlib.util.spec_from_file_location('v',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main():
 a=argparse.ArgumentParser();a.add_argument('--evidence',required=True);a.add_argument('--validator',required=True);a.add_argument('--out',required=True);x=a.parse_args();ep=pathlib.Path(x.evidence).resolve();root=ep.parent;d=json.loads(ep.read_text());why=[]
 if (d.get('schema'),d.get('mission_id'),d.get('issue'))!=('W2-ENG-TECHNICAL-S6-REMEDIATION-v1','W2-ENG-TECH-S6-REM-01',585):why+=['identity']
 rs=d.get('attempts',[])
 if [r.get('attempt') for r in rs]!=['N1','N2','FI1']:why+=['attempt_shape']
 else:
  for i,a in enumerate(['N1','N2']):
   r=rs[i];c=r['capture'];p=root/c['artifact'];q=pic(p)
   if q!={k:c[k] for k in ['sha256','size','format','dimensions','marker_rgb']} or q['format']!='PNG' or q['dimensions']!=[1280,720] or q['marker_rgb']!=RGB[a]:why+=[a+'_frame']
   b=r['binding'];
   if b['sha256']!=hd(b['body']) or b['body']['capture']['sha256']!=c['sha256'] or b['body']['attempt']!=a:why+=[a+'_binding']
  p1=root/rs[0]['capture']['artifact'];p2=root/rs[1]['capture']['artifact']
  if p1.read_bytes()==p2.read_bytes():why+=['frames_identical']
  with tempfile.TemporaryDirectory() as td:
   z=pathlib.Path(td)/'n2.png';z.write_bytes(p1.read_bytes());q=pic(z)
   if q['sha256']==rs[1]['capture']['sha256'] and q['marker_rgb']==RGB['N2']:why+=['substitution_not_rejected']
  fi=rs[2];c=fi['capture'];
  if not(fi['state_ok'] and fi['candidate_alive_at_capture'] and c['executed'] and pathlib.Path(c['command'][0]).name=='scrot' and c['exit']!=0 and c['frame_count']==0 and c['path_exists'] is False and c['failure_mode']=='REAL_SCROT_WRITE_TO_UNWRITABLE_PROC_PATH'):why+=['capture_down_not_observed']
 v=load(pathlib.Path(x.validator).resolve());av=v.va(v.adaptation('S6','Godot'),'Godot');agg=d.get('unchanged_v5',{}).get('aggregate')
 if av.get('result')!='ACCEPT' or agg!={'aggregate':'PASS_FOR_COMPARISON','reasons':[],'valid_envelope':True}:why+=['v5']
 if d.get('closed_findings')!=['W2-ENG-TECH-S6-REV-M01','W2-ENG-TECH-S6-REV-M02']:why+=['findings']
 out={'schema':'W2-ENG-TECHNICAL-S6-REMEDIATION-INDEPENDENT-VERIFY-v1','evidence_run_identity':d.get('run_identity'),'generation_id':d.get('generation_id'),'ok':not why,'reasons':sorted(set(why)),'actual_byte_substitution_rejected':'substitution_not_rejected' not in why,'capture_down_observed':'capture_down_not_observed' not in why,'recomputed_v5_adaptation':av,'recomputed_v5_aggregate':agg,'fresh_review_still_required':True,'canonicality':'NOT_CANONICAL'};pathlib.Path(x.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');return 0 if out['ok'] else 2
if __name__=='__main__':raise SystemExit(main())
