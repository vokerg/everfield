# W2-HASH-01 — Canonical Semantic Encoding and Cross-Runtime Hash Conformance

**Mission:** `W2-HASH-01`  
**Issue:** #73  
**Task class:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Candidate:** `ef-sem-1`  
**Result:** **PASS (BOUNDED)**  
**Canonicality:** NON-CANONICAL; `W2-REV-01` remains required  
**Production implementation / engine-selection authority:** NONE

## 1. Scope and non-goals

This experiment tests the Wave 1 `TECH-EV-HASH-CONFORMANCE` question: whether two separately implemented runtimes can derive identical canonical bytes and SHA-256 identity for a versioned engine-independent semantic value model across ordering, numbers, strings, defaults, references, schema/content identity, and rejection edges.

It does not select an engine, authorize gameplay/production implementation, define persistence bytes or migration, bless native JSON/runtime serializers, or upgrade review independence.

## 2. Candidate contract: `ef-sem-1`

The hash input is a canonical map containing `encoding_version`, `schema_id`, non-empty `schema_version`, stable `content_id`, lower-case 64-hex `content_hash`, and schema-materialized `value`.

Semantic forms:

- null `N;`; booleans `B0;` / `B1;`;
- signed i64 `I<canonical-decimal>;` (no `-0`, leading zero, or raw JSON/runtime number);
- fixed decimal `D<coefficient>@<scale>;` (no exponent, trailing fractional zeros stripped, `-0 -> 0@0`, coefficient i64, scale <= 18);
- string `S<byte_len>:<strict-utf8>` after Unicode-scalar validation; **no Unicode normalization**;
- reference `R` with framed non-empty namespace and stable ID; no pointer/path identity;
- list `L<count>[...]`, preserving order;
- map `M<count>{...}`, with string keys sorted by raw UTF-8 bytes and all keys/values length-framed.

The fixture schema requires `name`, materializes `enabled=true`, `quantity=0`, `price=0`, and rejects unknown fields. Schema/content identity is inside the hash scope, so version/content changes intentionally change identity.

Out of scope in v1: floats/NaN/Infinity, arbitrary precision integers, decimal scale >18, binary, sets, cycles/shared-object identity, ambient time, locale/case normalization, and runtime/editor object IDs. Adding any of these requires a versioned extension and new conformance evidence.

## 3. Experiment

Shared corpus: 29 adversarial fixtures (18 accepted, 11 rejected). Two independently written adapter implementations consumed the same transport corpus:

1. Python `3.13.5`, Unicode data `15.1.0`, `hashlib`, strict UTF-8.
2. Node `v22.16.0`, ICU `77.1`, Unicode `16.0`, `crypto`, explicit Unicode-scalar validation.

The adapters share no canonicalization code. Final comparison was exact equality of every case's accepted canonical bytes/hash or standardized rejection code.

**Final result:** Python and Node match on all **29/29** cases.

Key accepted relations/differences:

- `baseline == map-reordered`: `580ed39bc4b87373fff4c7e1715695be63a346bc233397f324c5a2bfdcc5ee7c`.
- explicit defaults == omitted defaults: `af639d11d325efd52381fcb74a34b794cd7f621081e0350819fc253613c75e91`.
- decimal `001.2300 == 1.23`: `4dddb134a8919f8f44228d4d925c1126ffb96961e6491f8d7bd7729f27598176`.
- composed Unicode: `2b8852f0cf741d5c1e8f5a601c8562d91ecd590dec848b9dc629e243162f4035`.
- decomposed Unicode: `619949d3c296ac59e91b7b3c2aaddb0e65d0e6793126f538ece6e6aa9bb96f6e` (intentionally distinct).
- list order A/B: `d86979e4acbe229bae98a72fe7197a7073e1b72aab6122717d0802b42dcbdee3` / `0b4343e9a602187e98d6b54f048507382c7da975196282bc85dcfb4d5cc6953f`.
- schema v1/v2: `1ee1a5ae84fb7723c8fed85b6194471205f4b4b4168b6cdb98c9e2428c7ed38a` / `cdd3b010a3c221e7f95aa772765447db29d279683b4408bb520561887076e532`.
- content A/B: `f92bb31ea53fdfd9add5a12a42d27587e7f30ae198786f5cb28f2b71c9a5c30b` / `b3445a65d64254b98385a673ec50a5d7682d23cd06bedaf7917a72207e033359`.
- i64 min/max accepted; negative zero decimal canonicalizes to `0@0`; control characters + emoji agree.

Rejected in both implementations with the same class: ambiguous integer syntax, i64 overflow, exponent decimal, excessive decimal scale, unpaired surrogate, unknown schema field, raw JSON number, empty reference component, malformed content hash, and empty schema version.

## 4. Retained mismatch evidence

Two implementation hazards were discovered rather than hidden:

1. **Unpaired surrogate divergence.** Python strict UTF-8 rejected `U+D800`; naive Node UTF-8 encoded replacement character `U+FFFD`. `ef-sem-1` therefore requires explicit Unicode-scalar validation before UTF-8. The retained fixture now produces `NON_SCALAR_STRING` in both adapters.
2. **Falsy defaulting bug.** An early Node `||` default would have changed explicit empty `schema_version` into version `1`. Presence-based defaulting fixed it; both adapters now reject `schema_version: ""` as `SCHEMA_VERSION`.

These are evidence that native runtime behavior must not substitute for the semantic contract.

## 5. Evidence vs inference and bounded disposition

Observed: all 29 final result objects agree; accepted bytes/hashes agree; rejection classes agree; Unicode runtime versions differ without affecting exact scalar-sequence identity; adversarial cases found two real adapter hazards before the final run.

Inference: this supports **cross-runtime semantic hash authority only for values conforming exactly to reviewed `ef-sem-1` plus the same schema/content materialization rules**. It does not authorize local/native serializer hashes, untested value classes, implicit normalization, engine selection, or implementation readiness.

**Disposition: PASS (bounded).** W2-REV-01 must independently attack framing ambiguity, numeric edges, Unicode/surrogate behavior, default materialization, schema/content scope, implementation diversity, fixture sufficiency, and downstream overclaiming.

## 6. Failure modes, unresolved questions, and reopen conditions

Reopen/version if a third conforming runtime disagrees; normalization/case folding becomes semantic; ranges/scales expand; floats/binary/sets/cycles/timestamps/new primitives become authoritative; schema default/unknown-field rules change; content identity derivation or hash algorithm/scope changes; reference identity changes; migration needs cross-version equivalence; scalar validation cannot be enforced; or retained artifact integrity/availability is lost.

Still unresolved: production schema registry/versioning, production content-package hashing, migration equivalence, persistence encoding, and which state scopes require hash comparison.

Downstream: after required review, this is the `W2-HASH-01` evidence input for `W2-ENG-03` and `W2-REV-01`. No downstream authority is created by authorship alone.

## 7. Retained ArtifactIdentity records

| artifact_id | SHA-256 content_hash | retention |
|---|---|---|
| `w2-hash-01-corpus-v1` | `527a5b70cf04ef5fef1ec3247c42364fe766792d0525105e62510656681aa2b7` | exact Appendix A |
| `w2-hash-01-python-adapter-v1` | `2b3619343d1d3a70da27070414f013c51392e4031224a455f81bb87a5bad3902` | exact Appendix B |
| `w2-hash-01-node-adapter-v1` | `791479f5a8d004da4dd6c111e05e89917ac87b840ff8dc02be7e6f6c0a3a89dc` | exact Appendix C |
| `w2-hash-01-python-run-v1` | `cf643bf2e5e76d27b3e29016954c04135477d7e0d6c3aa241ee5a5d765657f61` | final stdout JSON identity; reproducible from A+B |
| `w2-hash-01-node-run-v1` | `48ac0a2f952c178d2099f426c0669bd74f0ddf654f5121565b610ba4096a4e20` | final stdout JSON identity; reproducible from A+C |

All are NORMAL planning-evidence fixtures, rights/terms `NOT_APPLICABLE`; adapter code is disposable and `production_dependency_allowed: false`. The corpus and adapter sources are retained byte-for-byte below; hashes above are their exact file hashes.

Reproduction: run each adapter with Appendix A reconstructed as its input, then compare only the emitted `results` objects; runtime metadata intentionally differs.

## Appendix A — exact corpus

```json
{"version":"fixture-transport-1","cases":[{"id":"baseline","input":{"name":"iron","quantity":{"@i":"10"},"price":{"@d":"1.2300"},"target":{"@ref":["item","ore.iron"]},"tags":["ore","metal"],"meta":{"z":"last","a":"first","\u00e9":"composed-key","e\u0301":"decomposed-key"}}},{"id":"map-reordered","input":{"meta":{"e\u0301":"decomposed-key","\u00e9":"composed-key","a":"first","z":"last"},"tags":["ore","metal"],"target":{"@ref":["item","ore.iron"]},"price":{"@d":"1.23"},"quantity":{"@i":"10"},"name":"iron"}},{"id":"defaults-explicit","input":{"name":"defaults","enabled":true,"quantity":{"@i":"0"},"price":{"@d":"0.000"}}},{"id":"defaults-omitted","input":{"name":"defaults"}},{"id":"i64-min","input":{"name":"min","quantity":{"@i":"-9223372036854775808"}}},{"id":"i64-max","input":{"name":"max","quantity":{"@i":"9223372036854775807"}}},{"id":"int-negzero-reject","input":{"name":"bad","quantity":{"@i":"-0"}}},{"id":"int-leadingzero-reject","input":{"name":"bad","quantity":{"@i":"01"}}},{"id":"decimal-normal-a","input":{"name":"dec","price":{"@d":"001.2300"}}},{"id":"decimal-normal-b","input":{"name":"dec","price":{"@d":"1.23"}}},{"id":"decimal-negzero","input":{"name":"dz","price":{"@d":"-0.000"}}},{"id":"string-control-emoji","input":{"name":"line\n\u0000\ud83d\ude42"}},{"id":"unicode-composed","input":{"name":"\u00e9"}},{"id":"unicode-decomposed","input":{"name":"e\u0301"}},{"id":"string-unpaired-surrogate-reject","input":{"name":"\ud800"}},{"id":"list-order-a","input":{"name":"list","tags":["a","b"]}},{"id":"list-order-b","input":{"name":"list","tags":["b","a"]}},{"id":"schema-v1","schema_version":"v1","input":{"name":"identity"}},{"id":"schema-v2","schema_version":"v2","input":{"name":"identity"}},{"id":"content-a","content_hash":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","input":{"name":"identity"}},{"id":"content-b","content_hash":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","input":{"name":"identity"}},{"id":"unknown-field-reject","input":{"name":"bad","surprise":true}},{"id":"raw-number-reject","input":{"name":"bad","quantity":1}},{"id":"i64-overflow-reject","input":{"name":"bad","quantity":{"@i":"9223372036854775808"}}},{"id":"decimal-exp-reject","input":{"name":"bad","price":{"@d":"1e3"}}},{"id":"decimal-scale-overflow-reject","input":{"name":"bad","price":{"@d":"0.0000000000000000001"}}},{"id":"ref-empty-reject","input":{"name":"bad","target":{"@ref":["item",""]}}},{"id":"content-hash-invalid-reject","content_hash":"xyz","input":{"name":"bad"}},{"id":"schema-empty-reject","schema_version":"","input":{"name":"bad"}}]}```

## Appendix B — exact Python adapter

```python
import json, hashlib, sys, unicodedata
from dataclasses import dataclass

I64_MIN=-(2**63); I64_MAX=2**63-1
class E(Exception):
    def __init__(self, code): self.code=code; super().__init__(code)
@dataclass(frozen=True)
class I: v:int
@dataclass(frozen=True)
class D: coeff:int; scale:int
@dataclass(frozen=True)
class R: ns:str; id:str
DEFAULTS={'enabled': True,'quantity': I(0),'price': D(0,0)}
KNOWN={'name','enabled','quantity','price','target','notes','tags','meta'}

def fail(code): raise E(code)
def decimal(s):
    if not isinstance(s,str): fail('DECIMAL_TRANSPORT_TYPE')
    if 'e' in s.lower(): fail('DECIMAL_EXPONENT_FORBIDDEN')
    neg=False
    if s.startswith(('+','-')): neg=s[0]=='-'; s=s[1:]
    if not s or s.count('.')>1: fail('DECIMAL_SYNTAX')
    a,b=s.split('.',1) if '.' in s else (s,'')
    if not a: a='0'
    if not a.isdigit() or (b and not b.isdigit()): fail('DECIMAL_SYNTAX')
    coeff=int((a+b).lstrip('0') or '0'); scale=len(b)
    if neg: coeff=-coeff
    if coeff==0: return D(0,0)
    while scale>0 and coeff%10==0: coeff//=10; scale-=1
    if not I64_MIN<=coeff<=I64_MAX: fail('DECIMAL_COEFF_RANGE')
    if scale>18: fail('DECIMAL_SCALE_RANGE')
    return D(coeff,scale)

def parse(x):
    if x is None or isinstance(x,bool) or isinstance(x,str): return x
    if isinstance(x,(int,float)): fail('RAW_JSON_NUMBER_FORBIDDEN')
    if isinstance(x,list): return [parse(v) for v in x]
    if isinstance(x,dict):
        if len(x)==1 and '@i' in x:
            s=x['@i']
            if not isinstance(s,str) or not s or s=='-0' or (s.startswith('0') and s!='0') or s.startswith('-0') or not s.lstrip('-').isdigit(): fail('INTEGER_SYNTAX')
            v=int(s)
            if not I64_MIN<=v<=I64_MAX: fail('I64_RANGE')
            return I(v)
        if len(x)==1 and '@d' in x: return decimal(x['@d'])
        if len(x)==1 and '@ref' in x:
            a=x['@ref']
            if not isinstance(a,list) or len(a)!=2 or not all(isinstance(z,str) and z for z in a): fail('REF_SYNTAX')
            return R(a[0],a[1])
        return {k:parse(v) for k,v in x.items()}
    fail('TRANSPORT_TYPE')

def materialize(x):
    if not isinstance(x,dict): fail('RECORD_REQUIRED')
    if set(x)-KNOWN: fail('UNKNOWN_FIELD')
    if 'name' not in x or not isinstance(x['name'],str): fail('NAME_REQUIRED')
    y=dict(x)
    for k,v in DEFAULTS.items(): y.setdefault(k,v)
    return y

def utf8(s):
    if not isinstance(s,str): fail('STRING_REQUIRED')
    try: return s.encode('utf-8','strict')
    except UnicodeEncodeError: fail('NON_SCALAR_STRING')
def atom(tag,p): return tag+str(len(p)).encode()+b':'+p

def enc(v):
    if v is None: return b'N;'
    if v is False: return b'B0;'
    if v is True: return b'B1;'
    if isinstance(v,I): return b'I'+str(v.v).encode()+b';'
    if isinstance(v,D): return b'D'+str(v.coeff).encode()+b'@'+str(v.scale).encode()+b';'
    if isinstance(v,R): return b'R'+atom(b'n',utf8(v.ns))+atom(b'i',utf8(v.id))+b';'
    if isinstance(v,str): return atom(b'S',utf8(v))
    if isinstance(v,list): return b'L'+str(len(v)).encode()+b'['+b''.join(enc(z) for z in v)+b']'
    if isinstance(v,dict):
        items=sorted(((utf8(k),v) for k,v in v.items()), key=lambda kv:kv[0])
        return b'M'+str(len(items)).encode()+b'{'+b''.join(atom(b'K',k)+enc(val) for k,val in items)+b'}'
    fail('SEMANTIC_TYPE')

def envelope(v,sv='1',ch='a'*64):
    if not isinstance(sv,str) or not sv: fail('SCHEMA_VERSION')
    if not isinstance(ch,str) or len(ch)!=64 or any(c not in '0123456789abcdef' for c in ch): fail('CONTENT_HASH')
    return {'content_hash':ch,'content_id':'fixture-content','encoding_version':'ef-sem-1','schema_id':'everfield.fixture.record','schema_version':sv,'value':materialize(v)}
def run(c):
    try:
        b=enc(envelope(parse(c['input']),c.get('schema_version','1'),c.get('content_hash','a'*64)))
        return {'ok':True,'hash':hashlib.sha256(b).hexdigest(),'bytes_hex':b.hex()}
    except E as e: return {'ok':False,'error_code':e.code}
def main(path):
    corpus=json.load(open(path,encoding='utf-8'))
    print(json.dumps({'runtime':'python-'+sys.version.split()[0],'unicode':unicodedata.unidata_version,'results':{c['id']:run(c) for c in corpus['cases']}},sort_keys=True,separators=(',',':'),ensure_ascii=True))
if __name__=='__main__': main(sys.argv[1])
```

## Appendix C — exact Node adapter

```javascript
const fs=require('fs'),crypto=require('crypto');
const MIN=-(1n<<63n),MAX=(1n<<63n)-1n;
class E extends Error{constructor(code){super(code);this.code=code}}; class I{constructor(v){this.v=v}}; class D{constructor(c,s){this.coeff=c;this.scale=s}}; class R{constructor(ns,id){this.ns=ns;this.id=id}};
const DEFAULTS={enabled:true,quantity:new I(0n),price:new D(0n,0)},KNOWN=new Set(['name','enabled','quantity','price','target','notes','tags','meta']);
const fail=c=>{throw new E(c)};
function decimal(s){if(typeof s!=='string')fail('DECIMAL_TRANSPORT_TYPE');if(/[eE]/.test(s))fail('DECIMAL_EXPONENT_FORBIDDEN');let neg=false;if(s[0]=='+'||s[0]=='-'){neg=s[0]=='-';s=s.slice(1)}if(!s||(s.match(/\./g)||[]).length>1)fail('DECIMAL_SYNTAX');let [a,b='']=s.includes('.')?s.split('.',2):[s,''];if(!a)a='0';if(!/^\d+$/.test(a)||(b&&!/^\d+$/.test(b)))fail('DECIMAL_SYNTAX');let coeff=BigInt((a+b).replace(/^0+/,'')||'0'),scale=b.length;if(neg)coeff=-coeff;if(coeff===0n)return new D(0n,0);while(scale>0&&coeff%10n===0n){coeff/=10n;scale--}if(coeff<MIN||coeff>MAX)fail('DECIMAL_COEFF_RANGE');if(scale>18)fail('DECIMAL_SCALE_RANGE');return new D(coeff,scale)}
function parse(x){if(x===null||typeof x==='boolean'||typeof x==='string')return x;if(typeof x==='number')fail('RAW_JSON_NUMBER_FORBIDDEN');if(Array.isArray(x))return x.map(parse);if(typeof x==='object'){let ks=Object.keys(x);if(ks.length===1&&ks[0]==='@i'){let s=x['@i'];if(typeof s!=='string'||!s||s==='-0'||(s.startsWith('0')&&s!=='0')||s.startsWith('-0')||!s.replace(/^-/,'').match(/^\d+$/))fail('INTEGER_SYNTAX');let v=BigInt(s);if(v<MIN||v>MAX)fail('I64_RANGE');return new I(v)}if(ks.length===1&&ks[0]==='@d')return decimal(x['@d']);if(ks.length===1&&ks[0]==='@ref'){let a=x['@ref'];if(!Array.isArray(a)||a.length!==2||!a.every(z=>typeof z==='string'&&z.length))fail('REF_SYNTAX');return new R(a[0],a[1])}let o={};for(let k of ks)o[k]=parse(x[k]);return o}fail('TRANSPORT_TYPE')}
function materialize(x){if(x===null||Array.isArray(x)||typeof x!=='object'||x instanceof I||x instanceof D||x instanceof R)fail('RECORD_REQUIRED');for(let k of Object.keys(x))if(!KNOWN.has(k))fail('UNKNOWN_FIELD');if(typeof x.name!=='string')fail('NAME_REQUIRED');let y={...x};for(let [k,v] of Object.entries(DEFAULTS))if(!(k in y))y[k]=v;return y}
function scalarBytes(s){if(typeof s!=='string')fail('STRING_REQUIRED');for(const ch of s){const cp=ch.codePointAt(0);if(cp>=0xD800&&cp<=0xDFFF)fail('NON_SCALAR_STRING')}return Buffer.from(s,'utf8')}
const B=s=>Buffer.from(s,'ascii'),atom=(tag,p)=>Buffer.concat([B(tag),B(String(p.length)),B(':'),p]);
function enc(v){if(v===null)return B('N;');if(v===false)return B('B0;');if(v===true)return B('B1;');if(v instanceof I)return B('I'+v.v+';');if(v instanceof D)return B('D'+v.coeff+'@'+v.scale+';');if(v instanceof R)return Buffer.concat([B('R'),atom('n',scalarBytes(v.ns)),atom('i',scalarBytes(v.id)),B(';')]);if(typeof v==='string')return atom('S',scalarBytes(v));if(Array.isArray(v))return Buffer.concat([B('L'+v.length+'['),...v.map(enc),B(']')]);if(typeof v==='object'){let items=Object.keys(v).map(k=>[scalarBytes(k),v[k]]).sort((a,b)=>Buffer.compare(a[0],b[0]));let p=[B('M'+items.length+'{')];for(let [k,val] of items)p.push(atom('K',k),enc(val));p.push(B('}'));return Buffer.concat(p)}fail('SEMANTIC_TYPE')}
function envelope(v,sv='1',ch='a'.repeat(64)){if(typeof sv!=='string'||!sv)fail('SCHEMA_VERSION');if(typeof ch!=='string'||! /^[0-9a-f]{64}$/.test(ch))fail('CONTENT_HASH');return {content_hash:ch,content_id:'fixture-content',encoding_version:'ef-sem-1',schema_id:'everfield.fixture.record',schema_version:sv,value:materialize(v)}}
function run(c){try{let b=enc(envelope(parse(c.input),('schema_version' in c?c.schema_version:'1'),('content_hash' in c?c.content_hash:'a'.repeat(64))));return {ok:true,hash:crypto.createHash('sha256').update(b).digest('hex'),bytes_hex:b.toString('hex')}}catch(e){if(e instanceof E)return {ok:false,error_code:e.code};throw e}}
let corpus=JSON.parse(fs.readFileSync(process.argv[2],'utf8')),results={};for(let c of corpus.cases)results[c.id]=run(c);console.log(JSON.stringify({runtime:'node-'+process.version,icu:process.versions.icu,unicode:process.versions.unicode,results}));
```