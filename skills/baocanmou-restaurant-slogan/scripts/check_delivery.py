#!/usr/bin/env python3
"""Check the default ten-method/three-choice delivery, not literary quality."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = {'clarity', 'appetite', 'memory', 'brand', 'medium'}


def check(data):
    errors = []
    catalog = json.loads((ROOT / 'references/sources.json').read_text(encoding='utf-8'))
    masters = {x['id'] for x in catalog['masters']}
    if not isinstance(data, dict):
        return {'passed': False, 'errors': ['Delivery must be an object']}
    if data.get('schema_version') != '1.0':
        errors.append('schema_version must be 1.0')
    if data.get('status') not in ('complete', 'partial'):
        errors.append('status must be complete or partial')

    def required_text(obj, keys, label):
        for key in keys:
            if not isinstance(obj.get(key), str) or not obj[key].strip():
                errors.append(f'{label}: nonempty {key} required')

    brief = data.get('brief', {})
    if not isinstance(brief, dict):
        brief = {}; errors.append('brief must be an object')
    required_text(brief, ('brand', 'category', 'audience_scene', 'task'), 'brief')
    medium = brief.get('primary_medium')
    if not ((isinstance(medium, str) and medium.strip()) or
            (isinstance(medium, list) and medium and all(isinstance(x, str) and x.strip() for x in medium))):
        errors.append('brief: primary_medium must be text or a nonempty text array')
    facts = {}
    raw_facts = brief.get('facts', [])
    if not isinstance(raw_facts, list):
        raw_facts = []; errors.append('facts must be an array')
    for f in raw_facts:
        if not isinstance(f, dict):
            errors.append('fact must be an object'); continue
        key = f.get('id')
        if not isinstance(key, str) or not key or key in facts:
            errors.append('missing/duplicate fact id'); continue
        facts[key] = f
        required_text(f, ('text', 'source'), key)
        if f.get('status') not in ('provided', 'verified', 'unknown', 'fictional'):
            errors.append(f'{key}: invalid fact status')
        if f.get('status') == 'fictional' and brief.get('fictional') is not True:
            errors.append(f'{key}: fictional fact requires fictional brief label')
    if not facts:
        errors.append('At least one explicitly sourced fact required')

    raw = data.get('candidates', [])
    if not isinstance(raw, list):
        raw = []; errors.append('candidates must be an array')
    if len(raw) != 10:
        errors.append('Default delivery needs exactly 10 candidates')
    candidates, methods, lines = {}, [], set()
    for c in raw:
        if not isinstance(c, dict):
            errors.append('candidate must be an object'); continue
        key = c.get('id')
        if not isinstance(key, str) or not key or key in candidates:
            errors.append('missing/duplicate candidate id'); continue
        candidates[key] = c
        method = c.get('master_id')
        methods.append(method)
        if method not in masters:
            errors.append(f'{key}: unknown master_id')
        required_text(c, ('line', 'tradeoff'), key)
        line = c.get('line', '')
        if isinstance(line, str):
            if '\n' in line or '\r' in line:
                errors.append(f'{key}: one slogan line required')
            normal = re.sub(r'[\W_]+', '', line).casefold()
            if normal in lines:
                errors.append(f'{key}: duplicate slogan')
            lines.add(normal)
        app = c.get('application', {})
        if not isinstance(app, dict):
            app = {}; errors.append(f'{key}: application must be an object')
        required_text(app, ('principle', 'move', 'limit'), key)
        refs = c.get('fact_ids', [])
        if not isinstance(refs, list) or not refs or any(not isinstance(r, str) or r not in facts for r in refs):
            errors.append(f'{key}: valid fact_ids required'); refs = []
        state = c.get('eligibility')
        if state not in ('eligible', 'conditional', 'reject'):
            errors.append(f'{key}: invalid eligibility')
        if state == 'eligible' and any(facts[r]['status'] == 'unknown' for r in refs):
            errors.append(f'{key}: unknown facts cannot support eligible candidate')
        conditions = c.get('conditions')
        if not isinstance(conditions, list) or any(not isinstance(x, str) or not x.strip() for x in conditions):
            errors.append(f'{key}: conditions must be a text array')
        elif state in ('conditional', 'reject') and not conditions:
            errors.append(f'{key}: unresolved or rejected candidate needs a reason')
        scores = c.get('comparison', {})
        if not isinstance(scores, dict) or set(scores) != DIMENSIONS or any(v not in ('strong', 'medium', 'weak') for v in scores.values()):
            errors.append(f'{key}: five qualitative comparisons required')
    if len(methods) != 10 or len(set(m for m in methods if isinstance(m, str))) != 10 or any(m not in methods for m in masters):
        errors.append('Each of the 10 methods must appear exactly once')

    recs = data.get('recommendations', [])
    if not isinstance(recs, list):
        recs = []; errors.append('recommendations must be an array')
    if data.get('status') == 'complete' and len(recs) != 3:
        errors.append('Complete delivery needs exactly 3 recommendations')
    if data.get('status') == 'partial':
        required_text(data, ('shortage_reason',), 'partial delivery')
        if len(recs) >= 3:
            errors.append('Partial delivery must explain fewer than 3 choices')
    seen = set()
    for i, r in enumerate(recs, 1):
        if not isinstance(r, dict):
            errors.append('recommendation must be an object'); continue
        key = r.get('candidate_id')
        if not isinstance(key, str) or key not in candidates or key in seen:
            errors.append('recommendation must reference a unique listed candidate'); continue
        seen.add(key)
        if candidates[key].get('eligibility') != 'eligible':
            errors.append(f'{key}: only eligible candidates may be recommended')
        if r.get('rank') != i:
            errors.append(f'{key}: consecutive recommendation ranks required')
        required_text(r, ('reason', 'placement', 'condition', 'test'), key)
    validation = data.get('validation', {})
    if not isinstance(validation, dict):
        validation = {}; errors.append('validation must be an object')
    required_text(validation, ('consumer_test', 'similarity_search'), 'validation')
    return {'passed': not errors, 'errors': errors, 'candidate_count': len(raw),
            'recommendation_count': len(recs),
            'limits': 'Counts, identities, references and declared status only. Theory fidelity, semantic originality, factual truth and advertising effectiveness require editorial or real-world review.'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('delivery', type=Path)
    args = ap.parse_args()
    try:
        result = check(json.loads(args.delivery.read_text(encoding='utf-8')))
    except (OSError, ValueError, TypeError, KeyError) as e:
        result = {'passed': False, 'errors': [str(e)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
