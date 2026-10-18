#!/usr/bin/env python3
"""Reproduce the published finite checks in clean staging; no network or dependencies."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
HASH_FILE = 'SHA256_2026-10-18.json'
REPORT_FILE = 'VERIFICATION_2026-10-18.json'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, description):
    if not condition:
        raise RuntimeError(description)


def main():
    require(__debug__, 'Assertions must be enabled; do not run with -O or PYTHONOPTIMIZE.')
    manifest = json.loads((HERE / HASH_FILE).read_text())
    entries = manifest['files']
    for name, expected in entries.items():
        require(digest((HERE / name).read_bytes()) == expected, 'Hash mismatch: ' + name)
    env = dict(os.environ)
    env.pop('PYTHONOPTIMIZE', None)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    expected_outputs = json.loads((HERE / 'EXPECTED_OUTPUTS_2026-10-18.json').read_text())
    expected_by_output = {item['output']: item for item in expected_outputs['checks']}
    runs = [(item['script'], item['output'], item['channel'], item['cases'])
            for item in expected_outputs['checks']]
    reports = []
    negatives = []
    with tempfile.TemporaryDirectory(prefix='wilson-research-') as tmp:
        staging = Path(tmp) / 'results'
        staging.mkdir()
        for name in list(entries) + [HASH_FILE]:
            target = staging / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(HERE / name, target)
        require(all(not (staging / item['output']).exists() for item in expected_outputs['checks']),
                'Detailed generated outputs must be absent before the clean run')
        for script, saved, channel, count in runs:
            run = subprocess.run([sys.executable, '-B', script], cwd=staging, env=env, capture_output=True)
            require(run.returncode == 0, 'Checker failed: ' + script + '\n' + run.stderr.decode())
            generated = (staging / saved).read_bytes() if channel == 'file' else run.stdout
            require(digest(generated) == expected_by_output[saved]['sha256'], 'Generated output hash mismatch: ' + saved)
            actual = json.loads(generated)
            actual_count = len(actual) if isinstance(actual, list) else (actual['cases'] if isinstance(actual.get('cases'), int) else len(actual['cases']))
            require(actual_count == count, 'Unexpected case count: ' + script)
            reports.append({'script': script, 'status': 'PASS', 'cases': count, 'generated_output_sha256_matches': True})
        mutations = [
            ('cylinder_false_single_block_bound', runs[0][0], 'assert max(blocks)-min(blocks)<=1', 'assert max(blocks)-min(blocks)<=0'),
            ('tilted_false_vertex_count', runs[1][0], 'assert len(verts)==2*N**d', 'assert len(verts)==3*N**d'),
            ('straight_false_diagonal_index', runs[4][0], "assert indices=={'straight_coordinate':1,'straight_diagonal':2", "assert indices=={'straight_coordinate':1,'straight_diagonal':1"),
        ]
        for name, script, old, new in mutations:
            source = (HERE / script).read_text()
            require(source.count(old) == 1, 'Negative control mutation not uniquely located: ' + name)
            target = staging / ('negative_' + name + '.py')
            target.write_text(source.replace(old, new))
            run = subprocess.run([sys.executable, '-B', target.name], cwd=staging, env=env, capture_output=True, text=True)
            require(run.returncode != 0 and 'AssertionError' in run.stderr, 'False assertion was not rejected: ' + name)
            negatives.append({'name': name, 'status': 'PASS', 'expected_assertion_failure_observed': True})
        tamper_target = staging / runs[0][0]
        original = tamper_target.read_bytes()
        tamper_target.write_bytes(original + b'\n# deliberate integrity-test mutation\n')
        run = subprocess.run([sys.executable, '-B', 'verify_research_2026_10_18.py'], cwd=staging, env=env, capture_output=True, text=True)
        require(run.returncode != 0 and 'Hash mismatch:' in run.stderr, 'Full verifier did not reject changed bytes')
        tamper_target.write_bytes(original)
        negatives.append({'name': 'changed_bytes_hash_mismatch', 'status': 'PASS', 'full_verifier_rejected': True})
        run = subprocess.run([sys.executable, '-O', '-B', 'verify_research_2026_10_18.py'], cwd=staging, env=env, capture_output=True, text=True)
        require(run.returncode != 0 and 'Assertions must be enabled' in run.stderr, 'Full verifier did not reject disabled assertions')
        negatives.append({'name': 'disabled_assertions_rejected', 'status': 'PASS', 'full_verifier_rejected': True})
    report = {
        'status': 'PASS',
        'scope': 'Hash integrity and exact finite geometry checks only. Analytic and topological proofs remain written arguments.',
        'hashed_files': len(entries),
        'checker_runs': reports,
        'total_finite_cases': sum(item['cases'] for item in reports),
        'negative_controls': negatives,
        'clean_temporary_staging': True,
        'detailed_outputs_tracked_or_archived': False,
        'network_used': False,
    }
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
