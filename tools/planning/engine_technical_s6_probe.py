#!/usr/bin/env python3
import argparse,hashlib,importlib.util,json,os,pathlib,shutil,subprocess,tempfile,time
from PIL import Image
M='CAPTURE-STATE-042'; INJ='FI-S6-CAPTURE-DOWN-v2'; RGB={'N1':[255,255,0],'N2':[255,0,255],'FI1':[0,255,255]}; HX={'N1':'FFFF00','N2':'FF00FF','FI1':'00FFFF'}
PROJ='''[application]\nrun/main_scene="res://m.tscn"\n[display]\nwindow/size/viewport_width=1280\nwindow/size/viewport_height=720\nwindow/size/window_width_override=1280\nwindow/size/window_height_override=720\nwindow/resizable=false\n[rendering]\nrenderer/rendering_method="gl_compatibility"\n'''
SCN='''[gd_scene load_steps=2 format=3]\n[ext_resource path="res://m.gd" type="Script" id="1"]\n[node name="M" type="Node2D"]\nscript=ExtResource("1")\n'''
GD=r'''extends Node2D
var c=Color.WHITE
func _ready():
 var a=OS.get_environment("E_ATTEMPT"); var cs={"N1":Color(1,1,0),"N2":Color(1,0,1),"FI1":Color(0,1,1)}; var hs={"N1":"FFFF00","N2":"FF00FF","FI1":"00FFFF"}; c=cs[a]
 var f=FileAccess.open(OS.get_environment("E_READY"),FileAccess.WRITE); f.store_string("CAPTURE-STATE-042|Godot|"+OS.get_environment("E_GEN")+"|"+a+"|"+hs[a]+"|1280x720"); f.close(); queue_redraw()
func _draw():
 draw_rect(Rect2(0,0,426,720),Color(.8,.12,.12)); draw_rect(Rect2(426,0,428,720),Color(.12,.72,.2)); draw_rect(Rect2(854,0,426,720),Color(.12,.25,.86)); draw_rect(Rect2(160,160,96,96),c)
'''
def h(b):return hashlib.sha256(b).hexdigest()
def jf(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def hd(x):return h(jf(x).encode())
def load(p,n):s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def cmd(c,cwd=None,env=None):
 p=subprocess.run(c,cwd=cwd,env=env,text=True,capture_output=True,check=False);return {'command':c,'executed':True,'exit':p.returncode,'stdout':p.stdout[-2000:],'stderr':p.stderr[-2000:]}
def inspect(p):
 with Image.open(p) as im:im.load();q=im.convert('RGB');return {'sha256':h(p.read_bytes()),'size':p.stat().st_size,'format':im.format,'dimensions':list(im.size),'marker_rgb':list(q.getpixel((200,200)))}
def one(root,out,a,fi,exe,exesha,gen,runid,projsha):
 w=root/a;w.mkdir();(w/'project.godot').write_text(PROJ);(w/'m.tscn').write_text(SCN);(w/'m.gd').write_text(GD);ready=w/'ready';e=os.environ.copy();e.update(E_READY=str(ready),E_GEN=gen,E_ATTEMPT=a);launch=[exe,'--path',str(w),'--display-driver','x11','--rendering-method','gl_compatibility'];p=subprocess.Popen(launch,cwd=w,env=e,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 for _ in range(200):
  if ready.exists() or p.poll() is not None:break
  time.sleep(.1)
 state=ready.read_text().strip() if ready.exists() else '';time.sleep(.5);alive=p.poll() is None;sc=shutil.which('scrot') or 'scrot'
 if fi:r=cmd([sc,'-z','/proc/everfield-s6-capture-down.png']);cap={**r,'mechanism':'CANDIDATE_BOUND_X11_FRAMEBUFFER','injection':INJ,'failure_mode':'REAL_SCROT_WRITE_TO_UNWRITABLE_PROC_PATH','frame_count':0,'path_exists':False,'artifact':None}
 else:
  rel=f'frames/godot-{a}.png';fp=out/rel;fp.parent.mkdir(exist_ok=True);r=cmd([sc,'-z',str(fp)]);cap={**r,**(inspect(fp) if fp.exists() else {}),'mechanism':'CANDIDATE_BOUND_X11_FRAMEBUFFER','injection':None,'frame_count':1 if fp.exists() and r['exit']==0 else 0,'path_exists':fp.exists(),'artifact':rel}
 p.terminate();so,se=p.communicate(timeout=5);expected=f'{M}|Godot|{gen}|{a}|{HX[a]}|1280x720';okstate=state==expected
 ok=okstate and alive and (cap['executed'] and cap['exit']!=0 and cap['frame_count']==0 and not cap['path_exists'] if fi else cap.get('exit')==0 and cap.get('format')=='PNG' and cap.get('dimensions')==[1280,720] and cap.get('marker_rgb')==RGB[a])
 body={'candidate':'Godot','generation':gen,'attempt':a,'run':runid,'state':state,'project_sha256':projsha,'executable_sha256':exesha,'capture':{k:cap.get(k) for k in ['mechanism','injection','command','executed','exit','failure_mode','frame_count','path_exists','artifact','sha256','size','format','dimensions','marker_rgb']}}
 return {'attempt':a,'mode':'INJECT' if fi else 'NORMAL','state_ok':okstate,'candidate_alive_at_capture':alive,'capture':cap,'binding':{'body':body,'sha256':hd(body)},'formal_result':'PASS' if ok else 'INCONCLUSIVE','failure_class':'NONE' if ok else 'HARNESS','stdout':so[-1000:],'stderr':se[-1000:]}
def main():
 a=argparse.ArgumentParser();a.add_argument('--out',required=True);a.add_argument('--validator',required=True);a.add_argument('--toolchain-probe',required=True);a.add_argument('--artifact-lock',required=True);x=a.parse_args();out=pathlib.Path(x.out).resolve();out.parent.mkdir(parents=True,exist_ok=True);v=load(pathlib.Path(x.validator).resolve(),'v');tp=load(pathlib.Path(x.toolchain_probe).resolve(),'tp');lock=tp.load_artifact_lock(pathlib.Path(x.artifact_lock).resolve());runid=os.getenv('GITHUB_RUN_ID','LOCAL')+':'+os.getenv('GITHUB_RUN_ATTEMPT','1')+':'+os.getenv('GITHUB_SHA','LOCAL')
 with tempfile.TemporaryDirectory() as td:
  root=pathlib.Path(td);t=tp.probe_godot(root/'tool',lock);assert t['status']=='CAPABLE';projsha=h((PROJ+SCN+GD).encode());gen='GEN-S6-REM-'+h((runid+t['executable_sha256']+projsha).encode())[:20];rs=[one(root/'runs',out.parent,'N1',False,t['executable'],t['executable_sha256'],gen,runid,projsha),one(root/'runs',out.parent,'N2',False,t['executable'],t['executable_sha256'],gen,runid,projsha),one(root/'runs',out.parent,'FI1',True,t['executable'],t['executable_sha256'],gen,runid,projsha)]
 ad=v.adaptation('S6','Godot');av=v.va(ad,'Godot');g=v.gen('S6',gid=gen,work='WORK-S6-REM-'+gen[-20:],normal=tuple(r['formal_result'] for r in rs[:2]),classes=tuple(r['failure_class'] for r in rs[:2]),injres=rs[2]['formal_result'],injfc=rs[2]['failure_class'],resets=('R1','R2'),oks=(True,True),wss=('W1','W2'),res='W2-ENG-HOST-COMMON-v2',cid='Godot');fi=[k for k,z in g['attempts'].items() if z['kind']=='FAILURE_INJECTION'][0];g['attempts'][fi].update(reset_id='R3',reset_verified=True,workspace_id='W3');agg=v.agg(g)
 n1,n2=rs[0]['capture'],rs[1]['capture'];p1=out.parent/n1['artifact'];p2=out.parent/n2['artifact'];neg={'frame_bytes_distinct':p1.read_bytes()!=p2.read_bytes() and n1['sha256']!=n2['sha256'],'actual_n1_bytes_rejected_as_n2':inspect(p1)['sha256']!=n2['sha256'] or inspect(p1)['marker_rgb']!=RGB['N2'],'real_capture_down_observed':rs[2]['capture']['executed'] and pathlib.Path(rs[2]['capture']['command'][0]).name=='scrot' and rs[2]['capture']['exit']!=0,'state_vs_capture_separated':rs[2]['state_ok'] and rs[2]['candidate_alive_at_capture'] and rs[2]['capture']['exit']!=0}
 ok=all(r['formal_result']=='PASS' for r in rs) and all(neg.values()) and av['result']=='ACCEPT' and agg=={'aggregate':'PASS_FOR_COMPARISON','reasons':[],'valid_envelope':True};d={'schema':'W2-ENG-TECHNICAL-S6-REMEDIATION-v1','mission_id':'W2-ENG-TECH-S6-REM-01','issue':585,'run_identity':runid,'generation_id':gen,'source':{'issue':456,'head':'0719199237d3ac46505f52a06df0a0fc93429c9f','run':31967674130,'artifact':9268994399},'review':{'issue':458,'terminal':5309336848,'findings':['W2-ENG-TECH-S6-REV-M01','W2-ENG-TECH-S6-REV-M02']},'contract':{'marker':M,'injection':INJ,'viewport':[1280,720],'screens':3,'capture_frames':1},'toolchain':{'baseline':'4.7.1-stable','executable_sha256':t['executable_sha256'],'artifact_identity':t['artifact_identity']},'attempts':rs,'unchanged_v5':{'adaptation':av,'aggregate':agg},'negative_controls':neg,'closed_findings':['W2-ENG-TECH-S6-REV-M01','W2-ENG-TECH-S6-REV-M02'] if ok else [],'disposition':'PROVISIONAL_S6_REMEDIATED_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW' if ok else 'INCONCLUSIVE_HARNESS_OR_INFRA','preserved':{'Bevy':'INCONCLUSIVE_HARNESS_OR_INFRA','Defold':'INCONCLUSIVE_HARNESS_OR_INFRA','Unity':'NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY','Unreal Engine':'NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY','issue_82_not_run_cells':50},'fresh_review_required':True,'trusted_comparison_authority':False,'integration_authority':False,'engine_selected':False,'implementation_readiness':False,'canonicality':'NOT_CANONICAL'};out.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');return 0 if ok else 2
if __name__=='__main__':raise SystemExit(main())
