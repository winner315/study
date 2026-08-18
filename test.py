# # f-string 格式化
# name = "小明"
# score = 95.5
# print(f"姓名：{name},分数:{score}")
# # 字符串操作
# text = "  Hello, Python 世界！  "
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())
#
# # split 拆分 & join 拼接
# a ="apple,banana,orange".split(",")
# print(a)
# b = " | ".join(['a', 'b', 'c'])
# print(b)
import datetime
import shutil
from pathlib import Path
from pydoc import resolve
from typing import Optional


def ask(prompt: str, default: str = '') -> str:
    """交互式输入，支持默认值。"""
    if default:
        prompt = f'{prompt}（默认 {default}）：'
    else:
        prompt = f'{prompt}：'
    v = input(prompt).strip()
    if len(v) >= 2:
        if (v.startswith('"') and v.endswith('"')) or \
                (v.startswith("'") and v.endswith("'")):
            v = v[1:-1]
    return v if v else default
def backup(filepath:Path) -> Optional[Path]:
    if filepath.exists():
        ts = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        bak = filepath.with_suffix(f'{filepath.suffix}.bak-{ts}')
        shutil.copy2(filepath, bak)
        return bak
    return None
def read_text(filepath:Path) -> Optional[str]:
    if not filepath.exists():
        return ''
    with open(filepaths,'r',encoding='utf-8-sig') as f:
        return f.read()
# 交互问询文件目录
filepaths = Path(ask('请输入操作目录',r"D:\Desktop\G-Radar项目描述.md")).resolve()
# 备份文件
backup(filepaths)
# 读取文件内容
text = read_text(filepaths)
print(text)
