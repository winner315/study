from pathlib import Path

import shutil
from typing import Optional

# HOME = Path.home()
# NODE_INSTALL_DIR = HOME / '.codex' / 'node'
#
#
# def find_npm()->Optional[str]:
#     npm_path = shutil.which('npm') or shutil.which('npm.cmd')
#     if npm_path:
#         return npm_path
#     local_npm = NODE_INSTALL_DIR/'npm.cmd'
#     if local_npm.exists():
#         return str(local_npm)
#     return None
#
#
# paths = find_npm()
# print(paths)



from pathlib import Path
import shutil
import datetime

SETTINGS_FILE = Path('settings.txt')

def read_text(filepath: Path) -> str:
    if not filepath.exists():
        return ''
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_text(filepath: Path, content: str) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def backup(filepath: Path):
    if filepath.exists():
        ts = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        bak = filepath.with_suffix(filepath.suffix + ts+'.bak')
        shutil.copy2(filepath,bak)
        return bak
    return  None


def update_setting(key: str, value: str) -> None:
    file_content = read_text(SETTINGS_FILE)
    lines = file_content.split('\n')
    new_lines = []
    found = False
    for line in lines:
        if line.startswith(key+'='):
            new_lines.append(f'{key}={value}')
            found = True
        else:
            new_lines.append(line)
    if not found:
        new_lines.append(f'{key}={value}')
    new_content = '\n'.join(new_lines)

    if SETTINGS_FILE.exists():
        bak = backup(SETTINGS_FILE)
        if bak:
             print(f'已备份{bak}')

    write_text(SETTINGS_FILE, new_content)
    print(f'修改完成{new_content}')

def main():
    update_setting('theme', 'light')
    update_setting('language', 'zh-CN')


if __name__ == '__main__':
    main()