#!/usr/bin/env python3
"""Bounded Issue #433 correction entry: preserve retained Bevy lock root identity."""
from __future__ import annotations
import hashlib, importlib.util, pathlib, shutil

HERE=pathlib.Path(__file__).resolve()
BASE=HERE.with_name('engine_technical_s5_probe.py')

def sha(path):return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
def load(path,name):
 s=importlib.util.spec_from_file_location(name,path)
 if not s or not s.loader:raise RuntimeError(path)
 m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

m=load(BASE,'everfield_s5_base')
BASE_SHA=sha(BASE);ENTRY_SHA=sha(HERE)
# Exact retained Bevy Cargo.lock root package identity from the reviewed S3/S4 toolchain line.
m.BEVY_FILES['Cargo.toml']="""[package]\nname='everfield_bevy_probe'\nversion='0.0.0'\nedition='2024'\n[dependencies]\nbevy = { version = '=0.19.0', default-features = false }\n"""
_original_validate=m.validate_candidate

def validate_candidate(repo,candidate,tool,tool_root,expected_status,expected_label):
 if candidate!='Bevy':return _original_validate(repo,candidate,tool,tool_root,expected_status,expected_label)
 env={'EVERFIELD_S5_EXPECT_STATUS':expected_status,'EVERFIELD_S5_EXPECT_LABEL':expected_label}
 cargo=(tool.get('cargo') or {}).get('path') or shutil.which('cargo')
 if not cargo:return {'ok':False,'reason':'cargo_missing'}
 build=m.run([str(cargo),'build','--locked','--quiet'],cwd=repo,timeout=900)
 exe=repo/'target'/'debug'/'everfield_bevy_probe'
 execution=m.run([str(exe)],cwd=repo,env=env,timeout=120) if m.ok(build) and exe.exists() else None
 passed=m.ok(build) and m.ok(execution) and 'EVERFIELD_S5:PASS' in (((execution or {}).get('stdout') or '')+((execution or {}).get('stderr') or ''))
 return {'ok':passed,'build':m.semantic_result(build),'execution':m.semantic_result(execution) if execution else None,'executable_sha256':m.digest_file(exe) if exe.exists() else None}
m.validate_candidate=validate_candidate
_original_identity=m.toolchain_identity

def toolchain_identity(candidate,tool,validator_sha,runner_sha,run_identity):
 x=_original_identity(candidate,tool,validator_sha,ENTRY_SHA,run_identity)
 x['body']['base_runner_sha256']=BASE_SHA
 x['body']['correction_entry_sha256']=ENTRY_SHA
 x['identity_digest']='sha256:'+m.digest_obj(x['body'])
 return x
m.toolchain_identity=toolchain_identity
# Bind the top-level runner identity to this correction entry; base runner identity is separately retained above.
m.__file__=str(HERE)

if __name__=='__main__':
 raise SystemExit(m.main())
