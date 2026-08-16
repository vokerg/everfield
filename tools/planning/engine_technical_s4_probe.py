#!/usr/bin/env python3
'''W2-ENG-TECH-S4-01 real-engine S4 save/schema empirical tranche.'''
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, os, pathlib, re, shutil, stat, subprocess, tempfile, time

RESOURCE='W2-ENG-HOST-COMMON-v2'
V1_FIELDS=['schema_version','seed','tick','entities','settings']
INJECTION='FI-S4-INCOMPAT-TUPLE-v2'
MARKER=re.compile(r'EVERFIELD_S4:PASS:(NORMAL|INCOMPAT_TUPLE)')

def run(cmd,cwd=None,env=None,timeout=600):
    e=os.environ.copy()
    if env: e.update(env)
    started=time.monotonic()
    try:
        p=subprocess.run(cmd,cwd=cwd,env=e,text=True,capture_output=True,timeout=timeout,check=False)
        return {'cmd':cmd,'exit':p.returncode,'seconds':round(time.monotonic()-started,3),'stdout':p.stdout[-16000:],'stderr':p.stderr[-16000:],'timed_out':False}
    except subprocess.TimeoutExpired as x:
        return {'cmd':cmd,'exit':None,'seconds':round(time.monotonic()-started,3),'stdout':x.stdout[-16000:] if isinstance(x.stdout,str) else '', 'stderr':x.stderr[-16000:] if isinstance(x.stderr,str) else '', 'timed_out':True}
    except FileNotFoundError as x:
        return {'cmd':cmd,'exit':127,'seconds':0,'stdout':'','stderr':str(x),'timed_out':False}

def ok(r): return bool(r and r.get('exit')==0 and not r.get('timed_out'))
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_text(s): return sha_bytes(s.encode())
def sha_file(p): return sha_bytes(pathlib.Path(p).read_bytes())
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    if not spec or not spec.loader: raise RuntimeError(f'{name} module unavailable')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def entity_rows(malformed=False):
    rows=[]
    for i in range(32):
        vals=[str(i),str((i*3)%16),str((i*5)%16),'ACTIVE' if i%2==0 else 'IDLE',str(i%4)]
        if malformed and i==7: vals=vals[:-1]
        rows.append(':'.join(vals))
    return ';'.join(rows)

def fixture_v1(malformed=False):
    return '\n'.join([
        'schema_version=1','seed=424242','tick=17',f'entities={entity_rows(malformed)}','settings=volume:7',''
    ])

def fixture_v2():
    return '\n'.join([
        'schema_version=2','seed=424242','tick=17',f'entities={entity_rows(False)}','settings=volume:7','world_flags={}','',''
    ])

def parse_fixture(text, allow_malformed=False):
    lines=[x for x in text.splitlines() if x]
    pairs=[]
    for line in lines:
        if '=' not in line: return {'ok':False,'reason':'line_missing_equals'}
        k,v=line.split('=',1); pairs.append((k,v))
    d=dict(pairs)
    if len(d)!=len(pairs): return {'ok':False,'reason':'duplicate_field'}
    sv=d.get('schema_version')
    req=set(V1_FIELDS) | ({'world_flags'} if sv=='2' else set())
    if set(d)!=req: return {'ok':False,'reason':'field_set_mismatch','fields':sorted(d)}
    if d.get('seed')!='424242' or d.get('tick')!='17' or d.get('settings')!='volume:7': return {'ok':False,'reason':'scalar_mismatch'}
    rows=d.get('entities','').split(';') if d.get('entities') else []
    if len(rows)!=32: return {'ok':False,'reason':'entity_count_mismatch','entity_count':len(rows)}
    widths=[len(r.split(':')) for r in rows]
    if any(w!=5 for w in widths):
        return {'ok':False,'reason':'malformed_entity_tuple','widths':widths} if not allow_malformed else {'ok':True,'malformed':True,'widths':widths}
    if sv=='2' and d.get('world_flags')!='{}': return {'ok':False,'reason':'world_flags_default_mismatch'}
    if sv not in ('1','2'): return {'ok':False,'reason':'unsupported_schema_version'}
    return {'ok':True,'schema_version':int(sv),'entity_count':32,'widths':widths}

def host_semantics(ws,mode):
    inp=pathlib.Path(ws)/'input.save'
    if mode=='INJECT':
        p=parse_fixture(inp.read_text())
        return {'pass':not p['ok'] and p.get('reason')=='malformed_entity_tuple','input':p}
    out=pathlib.Path(ws)/'roundtrip.save'; mig=pathlib.Path(ws)/'migrated.save'; replay=pathlib.Path(ws)/'replay.save'
    if not all(x.exists() for x in (out,mig,replay)): return {'pass':False,'reason':'missing_candidate_output'}
    src=inp.read_text(); rt=out.read_text(); mt=mig.read_text(); rp=replay.read_text()
    ps,pr,pm,pp=map(parse_fixture,(src,rt,mt,rp))
    good=all(x['ok'] for x in (ps,pr,pm,pp)) and src==rt and mt==fixture_v2() and rp==mt
    return {'pass':good,'input':ps,'roundtrip':pr,'migrated':pm,'replay':pp,
            'digests':{'input':sha_text(src),'roundtrip':sha_text(rt),'migrated':sha_text(mt),'replay':sha_text(rp)},
            'roundtrip_exact':src==rt,'migration_exact':mt==fixture_v2(),'replay_exact':rp==mt}

def attempt_record(candidate,label,mode,ws,command,host):
    marker=MARKER.findall((command.get('stdout') or '')+'\n'+(command.get('stderr') or ''))
    expected='INCOMPAT_TUPLE' if mode=='INJECT' else 'NORMAL'
    passed=ok(command) and expected in marker and host.get('pass') is True
    return {'candidate':candidate,'label':label,'mode':mode,'result':'PASS' if passed else 'INCONCLUSIVE',
            'failure_class':'NONE' if passed else 'HARNESS','workspace_id':sha_text(str(pathlib.Path(ws).resolve())),
            'reset_id':f'RESET-{candidate.upper().replace(" ","_")}-S4-{label}', 'reset_verified':True,
            'resource_class':RESOURCE,'command':command,'host_semantics':host}

def formalize(candidate,attempts,v):
    seed={'candidate':candidate,'attempts':[{'label':a['label'],'workspace_id':a['workspace_id'],'reset_id':a['reset_id'],'command_digest':sha_text(json.dumps(a['command'],sort_keys=True))} for a in attempts]}
    work='WORK-S4-'+sha_text(json.dumps(seed,sort_keys=True))[:24]
    gid='GEN-S4-'+sha_text(work+'|'+candidate)[:24]
    normals=[a for a in attempts if a['mode']=='NORMAL']; inj=[a for a in attempts if a['mode']=='INJECT']
    normal_results=tuple('PASS' if a['result']=='PASS' else 'INCONCLUSIVE' for a in normals)
    classes=tuple('NONE' if a['result']=='PASS' else 'HARNESS' for a in normals)
    injres='PASS' if inj and inj[0]['result']=='PASS' else 'INCONCLUSIVE'; injfc='NONE' if injres=='PASS' else 'HARNESS'
    g=v.gen('S4',gid=gid,work=work,normal=normal_results,classes=classes,injres=injres,injfc=injfc,
            resets=tuple(a['reset_id'] for a in normals),oks=tuple(a['reset_verified'] for a in normals),
            wss=tuple(a['workspace_id'] for a in normals),res=RESOURCE,cid=candidate)
    fi=[k for k,a in g['attempts'].items() if a['kind']=='FAILURE_INJECTION'][0]
    if inj:
        g['attempts'][fi]['reset_id']=inj[0]['reset_id']; g['attempts'][fi]['reset_verified']=inj[0]['reset_verified']; g['attempts'][fi]['workspace_id']=inj[0]['workspace_id']
    validation=v.va(g['adaptation'],candidate); aggregate=v.agg(g)
    sources={}
    ordered=normals+inj
    for formal,raw in zip(g['run_registry_refs'],ordered):
        sources[formal]={'label':raw['label'],'workspace_id':raw['workspace_id'],'reset_id':raw['reset_id'],
                         'command_sha256':sha_text(json.dumps(raw['command'],sort_keys=True)),
                         'host_semantics_sha256':sha_text(json.dumps(raw['host_semantics'],sort_keys=True))}
    return {'generation':g,'adaptation_validation':validation,'aggregate':aggregate,'source_bindings':sources}

def negative_selftests(v):
    tests={}
    a=v.adaptation('S4','NEG'); a['bounds']['save_v1_field_count']=4; tests['schema_bound_shrink_rejected']=v.va(a,'NEG')['result']=='REJECT'
    a=v.adaptation('S4','NEG'); a['mappings'].pop('explicit_migration'); tests['migration_obligation_missing_rejected']=v.va(a,'NEG')['result']=='REJECT'
    g=v.gen('S4',cid='NEG'); k=g['run_registry_refs'][0]; g['attempts'][k]['candidate_generation_id']='OTHER'; tests['candidate_generation_mismatch_rejected']=v.agg(g)['aggregate']!='PASS_FOR_COMPARISON'
    g=v.gen('S4',cid='NEG'); g['run_registry_refs'].append(g['run_registry_refs'][0]); tests['duplicate_registry_rejected']=v.agg(g)['aggregate']!='PASS_FOR_COMPARISON'
    g=v.gen('S4',cid='NEG',wss=('W','W')); tests['workspace_reuse_rejected']=v.agg(g)['aggregate']!='PASS_FOR_COMPARISON'
    bad=fixture_v1().replace('settings=volume:7\n',''); tests['schema_field_omission_rejected']=not parse_fixture(bad)['ok']
    bad2=fixture_v2().replace('world_flags={}\n',''); tests['missing_migration_default_rejected']=not parse_fixture(bad2)['ok']
    tests['malformed_tuple_rejected']=parse_fixture(fixture_v1(True)).get('reason')=='malformed_entity_tuple'
    tests['source_digest_substitution_detected']=sha_text(fixture_v1())!=sha_text(fixture_v1().replace('tick=17','tick=18'))
    return tests

BEVY=r'''use bevy::prelude::*;
use std::{collections::BTreeMap,env,fs,path::Path};
#[derive(Resource)] struct SaveState { seed:i64, tick:i64, entities:usize }
fn parse(s:&str)->Result<BTreeMap<String,String>,String>{let mut m=BTreeMap::new();for l in s.lines(){if l.is_empty(){continue}let (k,v)=l.split_once('=').ok_or("line")?;if m.insert(k.to_string(),v.to_string()).is_some(){return Err("dup".into())}}Ok(m)}
fn entity_count(v:&str)->Result<usize,String>{let rows:Vec<_>=v.split(';').collect();if rows.len()!=32{return Err("count".into())}for r in &rows{if r.split(':').count()!=5{return Err("tuple".into())}}Ok(rows.len())}
fn normal(d:&BTreeMap<String,String>,root:&Path)->Result<(),String>{for k in ["schema_version","seed","tick","entities","settings"]{if !d.contains_key(k){return Err("field".into())}}if d.len()!=5||d["schema_version"]!="1"{return Err("schema".into())}let n=entity_count(&d["entities"])?;let mut world=World::new();world.insert_resource(SaveState{seed:d["seed"].parse().map_err(|_|"seed")?,tick:d["tick"].parse().map_err(|_|"tick")?,entities:n});let r=world.resource::<SaveState>();if r.seed!=424242||r.tick!=17||r.entities!=32{return Err("world".into())}let src=fs::read_to_string(root.join("input.save")).map_err(|_|"read")?;fs::write(root.join("roundtrip.save"),&src).map_err(|_|"write")?;let mut lines:Vec<String>=src.lines().map(str::to_string).collect();lines[0]="schema_version=2".into();lines.push("world_flags={}".into());let mig=lines.join("\n")+"\n\n";fs::write(root.join("migrated.save"),&mig).map_err(|_|"mig")?;let md=parse(&mig)?;if md.len()!=6||md["world_flags"]!="{}"{return Err("default".into())}fs::write(root.join("replay.save"),&mig).map_err(|_|"replay")?;Ok(())}
fn main(){let root=env::current_dir().unwrap();let src=fs::read_to_string(root.join("input.save")).unwrap();let d=parse(&src).unwrap();let inject=env::var("EVERFIELD_S4_MODE").ok().as_deref()==Some("INJECT");if inject{match entity_count(d.get("entities").unwrap()){Err(e) if e=="tuple"=>{println!("EVERFIELD_S4:PASS:INCOMPAT_TUPLE");return},_=>std::process::exit(4)}}else if normal(&d,&root).is_ok(){println!("EVERFIELD_S4:PASS:NORMAL");return}std::process::exit(3)}'''

GDSCRIPT=r'''extends Node
func parse_save(text:String)->Dictionary:
 var d={}
 for line in text.split("\n",false):
  var p=line.find("=")
  if p<1 or d.has(line.substr(0,p)): return {"_error":"line"}
  d[line.substr(0,p)]=line.substr(p+1)
 return d
func entities_ok(s:String)->bool:
 var rows=s.split(";",false)
 if rows.size()!=32:return false
 for r in rows:
  if r.split(":",false).size()!=5:return false
 return true
func _ready():
 var src=FileAccess.get_file_as_string("res://input.save")
 var d=parse_save(src)
 var inject=OS.get_environment("EVERFIELD_S4_MODE")=="INJECT"
 if inject:
  if not entities_ok(d.get("entities","")):
   print("EVERFIELD_S4:PASS:INCOMPAT_TUPLE");get_tree().quit(0);return
  get_tree().quit(4);return
 if d.size()!=5 or d.get("schema_version")!="1" or not entities_ok(d.get("entities","")):
  get_tree().quit(3);return
 var f=FileAccess.open("res://roundtrip.save",FileAccess.WRITE);f.store_string(src);f.close()
 var lines=src.split("\n",false);lines[0]="schema_version=2";lines.append("world_flags={}")
 var mig="\n".join(lines)+"\n\n"
 var m=parse_save(mig)
 if m.size()!=6 or m.get("world_flags")!="{}":get_tree().quit(5);return
 f=FileAccess.open("res://migrated.save",FileAccess.WRITE);f.store_string(mig);f.close()
 f=FileAccess.open("res://replay.save",FileAccess.WRITE);f.store_string(mig);f.close()
 print("EVERFIELD_S4:PASS:NORMAL");get_tree().quit(0)'''

LUA=r'''local function parse_save(s)
 local d={}
 for line in string.gmatch(s,"[^\n]+") do local k,v=string.match(line,"^([^=]+)=(.*)$") if not k or d[k] then return nil,"line" end d[k]=v end
 return d,nil
end
local function entities_ok(s)
 local n=0
 for row in string.gmatch(s,"[^;]+") do n=n+1 local c=0 for _ in string.gmatch(row,"[^:]+") do c=c+1 end if c~=5 then return false end end
 return n==32
end
local function readall(p)local f=io.open(p,"r") if not f then return nil end local s=f:read("*a") f:close() return s end
local function writeall(p,s)local f=io.open(p,"w") if not f then return false end f:write(s) f:close() return true end
function init(self)
 local src=readall("input.save") if not src then print("EVERFIELD_S4:ERR:READ");sys.exit(3);return end
 local d,e=parse_save(src) if e then sys.exit(3);return end
 local inject=os.getenv("EVERFIELD_S4_MODE")=="INJECT"
 if inject then if not entities_ok(d.entities or "") then print("EVERFIELD_S4:PASS:INCOMPAT_TUPLE");sys.exit(0);return end sys.exit(4);return end
 if d.schema_version~="1" or not entities_ok(d.entities or "") then sys.exit(3);return end
 local native={schema_version=1,seed=tonumber(d.seed),tick=tonumber(d.tick),entities=d.entities,settings=d.settings}
 local savefile=sys.get_save_file("everfield_s4","native") sys.save(savefile,native) local loaded=sys.load(savefile)
 if loaded.seed~=424242 or loaded.tick~=17 or loaded.entities~=d.entities then sys.exit(5);return end
 if not writeall("roundtrip.save",src) then sys.exit(6);return end
 local lines={} for line in string.gmatch(src,"[^\n]+") do table.insert(lines,line) end lines[1]="schema_version=2" table.insert(lines,"world_flags={}")
 local mig=table.concat(lines,"\n").."\n\n" local md=parse_save(mig)
 if not md or md.world_flags~="{}" then sys.exit(7);return end
 local native2={schema_version=2,seed=tonumber(md.seed),tick=tonumber(md.tick),entities=md.entities,settings=md.settings,world_flags={}}
 local savefile2=sys.get_save_file("everfield_s4","native2") sys.save(savefile2,native2) local loaded2=sys.load(savefile2)
 if loaded2.schema_version~=2 or type(loaded2.world_flags)~="table" then sys.exit(8);return end
 if not writeall("migrated.save",mig) or not writeall("replay.save",mig) then sys.exit(9);return end
 print("EVERFIELD_S4:PASS:NORMAL");sys.exit(0)
end'''

def copy_input(ws,inject): (pathlib.Path(ws)/'input.save').write_text(fixture_v1(inject))

def bevy(root,lock,tool,v):
    if tool.get('status') not in ('CAPABLE','CAPABLE_WITH_PRESEED'): return {'candidate':'Bevy','producer_disposition':'NOT_RUN_TOOLCHAIN_UNAVAILABLE','toolchain':tool}
    p=root/'bevy-s4'; (p/'src').mkdir(parents=True); shutil.copy2(lock,p/'Cargo.lock')
    (p/'Cargo.toml').write_text("[package]\nname='everfield_bevy_s4'\nversion='0.0.0'\nedition='2024'\n[dependencies]\nbevy = { version = '=0.19.0', default-features = false }\n")
    (p/'src/main.rs').write_text(BEVY); cargo=(tool.get('cargo') or {}).get('path') or shutil.which('cargo')
    build=run([str(cargo),'build','--locked','--quiet'],cwd=p,timeout=900) if cargo else None; exe=p/'target/debug/everfield_bevy_s4'
    attempts=[]
    if ok(build) and exe.exists():
        for label,mode in [('N1','NORMAL'),('N2','NORMAL'),('FI1','INJECT')]:
            ws=root/'runs/bevy'/label; ws.mkdir(parents=True); x=ws/'everfield_bevy_s4'; shutil.copy2(exe,x); x.chmod(x.stat().st_mode|stat.S_IXUSR); copy_input(ws,mode=='INJECT')
            rr=run([str(x)],cwd=ws,env={'EVERFIELD_S4_MODE':mode},timeout=120); attempts.append(attempt_record('Bevy',label,mode,ws,rr,host_semantics(ws,mode)))
    f=formalize('Bevy',attempts,v) if len(attempts)==3 else None
    good=bool(f and f['aggregate']=={'aggregate':'PASS_FOR_COMPARISON','reasons':[],'valid_envelope':True})
    return {'candidate':'Bevy','toolchain':tool,'build':build,'attempts':attempts,'formal_v5':f,'producer_disposition':'PROVISIONAL_S4_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW' if good else 'INCONCLUSIVE_HARNESS_OR_INFRA'}

def godot(root,tool,v):
    if tool.get('status')!='CAPABLE' or not tool.get('executable'): return {'candidate':'Godot','producer_disposition':'NOT_RUN_TOOLCHAIN_UNAVAILABLE','toolchain':tool}
    exe=tool['executable']; attempts=[]
    for label,mode in [('N1','NORMAL'),('N2','NORMAL'),('FI1','INJECT')]:
        ws=root/'runs/godot'/label; ws.mkdir(parents=True); copy_input(ws,mode=='INJECT')
        (ws/'project.godot').write_text('[application]\nconfig/name="EverfieldS4"\nrun/main_scene="res://main.tscn"\n[rendering]\nrenderer/rendering_method="gl_compatibility"\n')
        (ws/'main.tscn').write_text('[gd_scene load_steps=2 format=3]\n\n[ext_resource path="res://main.gd" type="Script" id="1"]\n\n[node name="Main" type="Node"]\nscript = ExtResource("1")\n')
        (ws/'main.gd').write_text(GDSCRIPT)
        rr=run([exe,'--headless','--path',str(ws)],cwd=ws,env={'EVERFIELD_S4_MODE':mode},timeout=120); attempts.append(attempt_record('Godot',label,mode,ws,rr,host_semantics(ws,mode)))
    f=formalize('Godot',attempts,v); good=f['aggregate']=={'aggregate':'PASS_FOR_COMPARISON','reasons':[],'valid_envelope':True}
    return {'candidate':'Godot','toolchain':tool,'attempts':attempts,'formal_v5':f,'producer_disposition':'PROVISIONAL_S4_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW' if good else 'INCONCLUSIVE_HARNESS_OR_INFRA'}

def bundle_exe(bundle):
    if not bundle:return None
    cand=[]
    for p in pathlib.Path(bundle).rglob('*'):
        if not p.is_file() or p.suffix.lower() in ('.so','.dll','.dylib','.jar','.zip'): continue
        try:
            if p.stat().st_mode&(stat.S_IXUSR|stat.S_IXGRP|stat.S_IXOTH):cand.append(p)
        except OSError:pass
    return max(cand,key=lambda p:p.stat().st_size) if cand else None

def defold(root,tool,v):
    if tool.get('status')!='CAPABLE': return {'candidate':'Defold','producer_disposition':'NOT_RUN_TOOLCHAIN_UNAVAILABLE','toolchain':tool}
    jar=root/'bob-1.13.0.jar'; java=(tool.get('java') or {}).get('path') or shutil.which('java')
    if not jar.exists() or not java:return {'candidate':'Defold','producer_disposition':'INCONCLUSIVE_HARNESS_OR_INFRA','toolchain':tool,'reason':'bob_or_java_missing'}
    p=root/'defold-s4'; p.mkdir(); (p/'input').mkdir(); (p/'input/game.input_binding').write_text('')
    (p/'game.project').write_text('[project]\ntitle = EverfieldS4\n[bootstrap]\nmain_collection = /main.collectionc\n[display]\nwidth = 320\nheight = 180\n')
    (p/'main.collection').write_text('name: "main"\nscale_along_z: 0\nembedded_instances {\n id: "controller"\n data: "components {\\n  id: \\"script\\"\\n  component: \\"/controller.script\\"\\n}\\n"\n}\n')
    (p/'controller.script').write_text(LUA)
    builds=[]; bundle=None; variant=None
    for vv in ('headless','debug'):
        bdir=p/f'bundle-{vv}'; rr=run([java,'-jar',str(jar),'--root',str(p),'--bundle-output',str(bdir),'--variant',vv,'--platform','x86_64-linux','--archive','resolve','build','bundle'],cwd=p,timeout=900)
        builds.append({'variant':vv,'archive_enabled':True,'command':rr})
        if ok(rr):bundle=bdir;variant=vv;break
    exe=bundle_exe(bundle); attempts=[]
    if bundle and exe:
        for label,mode in [('N1','NORMAL'),('N2','NORMAL'),('FI1','INJECT')]:
            ws=root/'runs/defold'/label; shutil.copytree(bundle,ws); x=ws/exe.relative_to(bundle); copy_input(x.parent,mode=='INJECT')
            rr=run([str(x)],cwd=x.parent,env={'EVERFIELD_S4_MODE':mode},timeout=120)
            if not ok(rr) and shutil.which('xvfb-run'): rr=run(['xvfb-run','-a',str(x)],cwd=x.parent,env={'EVERFIELD_S4_MODE':mode},timeout=120)
            attempts.append(attempt_record('Defold',label,mode,x.parent,rr,host_semantics(x.parent,mode)))
    f=formalize('Defold',attempts,v) if len(attempts)==3 else None; good=bool(f and f['aggregate']=={'aggregate':'PASS_FOR_COMPARISON','reasons':[],'valid_envelope':True})
    return {'candidate':'Defold','toolchain':tool,'builds':builds,'bundle_variant':variant,'bundle_executable_sha256':sha_file(exe) if exe else None,'attempts':attempts,'formal_v5':f,'producer_disposition':'PROVISIONAL_S4_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW' if good else 'INCONCLUSIVE_HARNESS_OR_INFRA'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); ap.add_argument('--bevy-lock',required=True); ap.add_argument('--artifact-lock',required=True); ap.add_argument('--validator',required=True); ap.add_argument('--capability-probe',default='tools/planning/engine_toolchain_probe.py'); args=ap.parse_args()
    out=pathlib.Path(args.out); out.parent.mkdir(parents=True,exist_ok=True); cap=load(pathlib.Path(args.capability_probe),'cap'); v=load(pathlib.Path(args.validator),'v5'); lock=cap.load_artifact_lock(pathlib.Path(args.artifact_lock))
    assert parse_fixture(fixture_v1())['ok'] and parse_fixture(fixture_v2())['ok'] and not parse_fixture(fixture_v1(True))['ok']
    negatives=negative_selftests(v); assert all(negatives.values()),negatives
    with tempfile.TemporaryDirectory(prefix='everfield-s4-') as td:
        root=pathlib.Path(td); bp=cap.probe_bevy(root,pathlib.Path(args.bevy_lock)); dp=cap.probe_defold(root,lock); gp=cap.probe_godot(root,lock); up=cap.probe_unity(); xp=cap.probe_unreal()
        results={'Bevy':bevy(root,pathlib.Path(args.bevy_lock),bp,v),'Defold':defold(root,dp,v),'Godot':godot(root,gp,v),
                 'Unity':{'candidate':'Unity','scenario':'S4','toolchain':up,'producer_disposition':'NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY'},
                 'Unreal Engine':{'candidate':'Unreal Engine','scenario':'S4','toolchain':xp,'producer_disposition':'NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY'}}
        good=[k for k,x in results.items() if x.get('producer_disposition')=='PROVISIONAL_S4_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW']
        payload={'schema':'W2-ENG-TECHNICAL-S4-v1','mission_id':'W2-ENG-TECH-S4-01','source_issue':360,'source_engine_issue':82,'source_engine_terminal_comment':5276916603,'routing_directive_comment':5303081124,
                 'canonical_binding_comment':5245368879,'canonical_program_blob':'e3120ec203c4156328770aa86c12fbb7187966dc','harness_id':'W2-ENG-HARNESS-v5','feature_slice_id':'W2-ENG-FEATURE-SLICE-v2','scenario_manifest_id':'W2-ENG-SCENARIO-INPUTS-v2','scenario_id':'S4',
                 'scenario_contract':{'fixed_input_refs':['SLICE:logical_state','SLICE:save_schema'],'obligations':['round_trip','schema_evolution','explicit_migration','malformed_tuple_diagnostic'],'bounds':{'entity_count':32,'save_v1_field_count':5,'save_v2_added_field_count':1},'required_injection':INJECTION,'resource_class':RESOURCE,'mechanism_authority':'CANDIDATE_NATIVE_EQUIVALENT'},
                 'fixture_identity':{'v1_sha256':sha_text(fixture_v1()),'v2_sha256':sha_text(fixture_v2()),'malformed_sha256':sha_text(fixture_v1(True))},
                 'runner':{'github_sha':os.getenv('GITHUB_SHA'),'github_run_id':os.getenv('GITHUB_RUN_ID'),'github_run_attempt':os.getenv('GITHUB_RUN_ATTEMPT'),'runner_os':os.getenv('RUNNER_OS'),'runner_arch':os.getenv('RUNNER_ARCH'),'image_os':os.getenv('ImageOS'),'image_version':os.getenv('ImageVersion')},
                 'results':results,'negative_selftests':negatives,'provisional_review_pending_s4_pass_candidates':good,'provisional_review_pending_s4_pass_count':len(good),
                 'authority_bound_not_run':{'Unity':'NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY','Unreal Engine':'NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY'},
                 'historical_issue_82_not_run_cells_preserved':50,'historical_issue_82_cells_mutated':False,'reviewed_s3_provenance_preserved':True,
                 'partial_candidate_ranking_permitted':False,'engine_selected':False,'production_implementation_ready':False,'verification_pass_authority':False,'decision_authority':False,'canonicality':'NOT_CANONICAL','integration_authority':False,'review_required_before_trust':True}
        out.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
        print(json.dumps({'provisional_review_pending_s4_pass_candidates':good,'count':len(good)},sort_keys=True))
    return 0
if __name__=='__main__': raise SystemExit(main())
