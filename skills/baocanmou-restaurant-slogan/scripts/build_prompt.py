#!/usr/bin/env python3
"""把 SKILL.md 和它引用的中文参考文件合并成一份聊天版提示词 PROMPT.md。

给不能加载 Skill 的聊天窗口用：DeepSeek、Kimi、豆包、通义千问、文心等。
改了 SKILL.md 或参考文件后重新运行；加 --check 只检查 PROMPT.md 是否需要重新生成。
"""
import posixpath
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOB = 'https://github.com/baocanmou/baocanmou-restaurant-slogan/blob/main/skills/baocanmou-restaurant-slogan'
TITLE = '包参谋·餐饮广告语：十法三选（聊天版）'
CHAT_RULES = """\
你现在按下面的“包参谋·餐饮广告语：十法三选”方法工作。你在聊天窗口里，不能运行脚本，也不能读写文件，所以：

- 不保存 delivery.json，不运行检查脚本，交付前按第 4、5 节人工复查：10 条、10 位作者、3 条推荐，来源和适用状态一一对应。
- 文中提到的中文参考文件都附在本文后面，按附录标题查找。英文执行说明没有附上；用户要英文广告语时，同样按中文方法卡执行，用自然的英文写。
- 联网检索近似表达前先征得用户同意；不能联网或没检索时标“未检索”。
- 用户还没讲餐饮情况时，先问一个简短问题：“这家店卖什么、顾客通常什么时候来吃、有什么能确认的特点、这句话准备放在哪里？”"""

USAGE = ('> 用法：复制本文件全文，作为第一条消息发给 AI（DeepSeek、Kimi、豆包、通义千问、文心等），'
         '或作为附件上传后说“按这个文件做”，再讲你的店。\n'
         '> 本文件由 `scripts/build_prompt.py` 从 SKILL.md 生成，要改请改源文件后重新生成。')

LINK = re.compile(r'( ?)\[([^\]]+)\]\((?![A-Za-z][A-Za-z0-9+.-]*:|#)([^)\s]+)\)( ?)')
SKIP = re.compile(r'\.en\.md$')


def rewrite(text, base, refs):
    def sub(match):
        before, label, target, after = match.groups()
        path = posixpath.normpath(posixpath.join(base, target))
        if path in refs:
            return f'附录《{refs[path]}》'
        if SKIP.search(path):
            return f'{before}{label}{after}'
        return f'{before}[{label}]({BLOB}/{path}){after}'
    return LINK.sub(sub, text)


def build():
    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    body = re.sub(r'\A---\n.*?\n---\n', '', skill, flags=re.S).strip()
    refs = {}
    for _, label, target, _ in LINK.findall(body):
        if target.startswith('references/') and target.endswith('.md') and not SKIP.search(target):
            refs.setdefault(target, label)
    parts = [f'# {TITLE}', USAGE, CHAT_RULES, '---', rewrite(body, '', refs)]
    for path, label in refs.items():
        ref = (ROOT / path).read_text(encoding='utf-8').strip()
        ref = re.sub(r'\A# .*\n+', '', ref)
        parts += ['---', f'# 附录《{label}》', rewrite(ref, posixpath.dirname(path), refs)]
    return '\n\n'.join(parts) + '\n'


def main():
    out = ROOT / 'PROMPT.md'
    text = build()
    if '--check' in sys.argv:
        if not out.exists() or out.read_text(encoding='utf-8') != text:
            print('PROMPT.md 已过期，请运行 python3 scripts/build_prompt.py')
            return 1
        print('PROMPT.md 是最新的')
        return 0
    out.write_text(text, encoding='utf-8')
    print(f'已生成 {out.name}，{len(text)} 字符')
    return 0


if __name__ == '__main__':
    sys.exit(main())
