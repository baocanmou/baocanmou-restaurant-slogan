#!/usr/bin/env python3
"""Offline checks for release completeness and example consistency, not quality."""
import importlib.util
import json
import re
import struct
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'baocanmou-restaurant-slogan'


def main():
    errors = []
    required = ['README.md', 'README.en.md', 'LICENSE', 'NOTICE.md', 'CITATION.cff',
                'PRIVACY.md', 'CONTRIBUTING.md', 'SECURITY.md', 'CHANGELOG.md',
                'docs/INSTALL.md', 'docs/USAGE.md', 'docs/ATTRIBUTION.md',
                'docs/MEDIA-KIT.md', 'docs/VALIDATION.md']
    for rel in required:
        if not (ROOT / rel).is_file():
            errors.append('Missing ' + rel)
    manifest = json.loads((ROOT / '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
    if manifest['name'] != 'baocanmou-restaurant-slogan' or manifest['version'] != '1.1.1':
        errors.append('Unexpected name/version')
    if not manifest.get('author', {}).get('name') or manifest.get('license') != 'MIT':
        errors.append('Author/license required')
    for field in ['composerIcon', 'logo', 'logoDark']:
        if not (ROOT / manifest['interface'][field]).is_file():
            errors.append('Missing icon: ' + field)
    for rel in manifest['interface']['screenshots']:
        path = ROOT / rel
        if not path.is_file():
            errors.append('Missing image: ' + rel)
        else:
            data = path.read_bytes()
            if data[:8] != b'\x89PNG\r\n\x1a\n' or min(struct.unpack('>II', data[16:24])) < 500:
                errors.append('Invalid/tiny screenshot: ' + rel)
    for lang in ['masters.en.md', 'restaurant.en.md', 'selection.en.md', 'workflow.en.md']:
        if not (SKILL / 'references' / lang).is_file():
            errors.append('Missing English execution guide: ' + lang)
    source = json.loads((SKILL / 'references/sources.json').read_text(encoding='utf-8'))
    if len({m['id'] for m in source['masters']}) != 10:
        errors.append('Need ten source-based methods')
    module_spec = importlib.util.spec_from_file_location('delivery_checker', SKILL / 'scripts/check_delivery.py')
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    samples = [SKILL / 'examples/delivery.json', SKILL / 'examples/tea-delivery.json',
               ROOT / 'examples/late-wok.en.json']
    for sample in samples:
        if not sample.is_file():
            errors.append('Missing example: ' + str(sample.relative_to(ROOT)))
            continue
        result = module.check(json.loads(sample.read_text(encoding='utf-8')))
        errors.extend(str(sample.relative_to(ROOT)) + ': ' + e for e in result['errors'])
    text_files = 0
    for path in ROOT.rglob('*'):
        if any(x in path.parts for x in ['.git', '__pycache__', 'dist', 'node_modules']):
            continue
        if path.suffix not in ['.md', '.json', '.yaml', '.yml', '.html', '.svg', '.cff']:
            continue
        text = path.read_text(encoding='utf-8'); text_files += 1
        if '/Users/' in text or '/Volumes/' in text or '[TODO:' in text:
            errors.append('Private path/unfinished marker: ' + str(path.relative_to(ROOT)))
        if re.search(r'(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{24,})', text):
            errors.append('Possible credential: ' + str(path.relative_to(ROOT)))
        if path.suffix == '.md':
            for match in re.finditer(r'\]\(([^)\n]+)\)', text):
                target = match.group(1).split(' "')[0].strip('<>')
                if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', target) or target.startswith('#'):
                    continue
                target = unquote(target.split('#')[0])
                if target and not (path.parent / target).exists():
                    errors.append(f'Broken local link in {path.relative_to(ROOT)}: {target}')
    print(json.dumps({'passed': not errors, 'text_files_checked': text_files,
                      'examples_checked': len(samples), 'errors': errors},
                     ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == '__main__':
    main()
