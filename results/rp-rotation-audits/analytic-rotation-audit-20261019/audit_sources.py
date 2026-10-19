#!/usr/bin/env python3
"""Read-only source audit and exact bump calculations. Written for this audit."""
from pathlib import Path
import hashlib, json, re
from fractions import Fraction
from math import comb, pi, sqrt

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / 'ym4-tilted-compatibility-20261018'
PIN = '785a68fdeef78a1da854c4807fe1f17b597d05e7'
ROOT = f'https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/{PIN}/'
raw_paths = {f'raw_{p}.tex': f'theorem_0_complete_account_raw_{p}.tex' for p in ['I','II','III']}
pdf_paths = {n: 'QED3_slop/'+n for n in ['YM_Rotation_Invariance_simplified.pdf','qed3_manuscript.pdf','qed3.pdf','qed3-consequences.pdf']}
manifest = {'upstream_commit': PIN, 'sources': []}
for directory, paths in [(RAW,raw_paths),(HERE,pdf_paths)]:
    for name, upstream in paths.items():
        data=(directory/name).read_bytes()
        git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
        manifest['sources'].append({'local':str(directory/name),'upstream_path':upstream,'url':ROOT+upstream,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob_sha':git_blob})
(HERE/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')

phrases = ['hyperoctahedrally','sixteen mirrors','diagonal reflection positivity','theorem deducing two-point']
hits=[]
for name in raw_paths:
    for lineno,line in enumerate((RAW/name).read_text().splitlines(),1):
        if any(p.casefold() in line.casefold() for p in phrases):
            hits.append({'source':name,'line':lineno,'text':line})
(HERE/'RAW_SEARCH_HITS.json').write_text(json.dumps({'literal_searches':phrases,'hits':hits},indent=2)+'\n')

extracts={'raw_I.tex':[(690,750),(1126,1205),(2512,2532),(2597,2621),(2689,2713),(2715,2820)],'raw_III.tex':[(79931,79990),(109237,109335)]}
out=[]
for name,ranges in extracts.items():
    lines=(RAW/name).read_text().splitlines()
    for start,end in ranges:
        out.append(f'\n===== {name}:{start}-{end} =====\n')
        out.extend(f'{i}: {lines[i-1]}' for i in range(start,end+1))
(HERE/'PINNED_EXTRACTS.txt').write_text('\n'.join(out)+'\n')

# Exact radial integrals: surface area S^3 = 2*pi^2.
radial=lambda k:sum((Fraction((-1)**j*comb(k,j),4+2*j) for j in range(k+1)), Fraction())
assert 2*radial(2)==Fraction(1,12)
assert 2*radial(4)==Fraction(1,30)
lip=8/(3*sqrt(3))
assert pi*pi/12>0.5 and lip<2
checks={'phi':'(1-|x|^2)_+^2','regularity':'C^1_c(R^4)','theta':0.5,'sup_norm':1,'L1_over_d4':'pi^2/12','L2_squared_over_d4':'pi^2/30','Lip_times_d':'8/(3 sqrt(3))','separation_over_d':2,'Gaussian_covariance_upper':'(C pi^2/15) d^4','exact_radial_checks_passed':True}
(HERE/'CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({'source_count':len(manifest['sources']),'literal_hits':len(hits),'checks':checks},indent=2))
