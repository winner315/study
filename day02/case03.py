# =================================================python 配置小助手===================================================================
import sys
import subprocess
import ctypes
import datetime
from pathlib import Path
import shutil


# ============ 工具函数（已写好，你不用改）============

def ask(prompt: str, default: str = '') -> str:
    if default:
        prompt = f'{prompt}（默认 {default}）：'
    else:
        prompt = f'{prompt}：'
    v = input(prompt).strip()
    return v if v else default


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
    """备份文件，返回备份路径，文件不存在返回 None。"""
    if filepath.exists():
        ts = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        bak = filepath.with_suffix(f'{filepath.suffix}.bak-{ts}')
        shutil.copy2(filepath, bak)
        return bak
    return None


def save_setting(name: str, value: str) -> bool:
    """保存配置到注册表 HKCU\Software\PythonHelper。"""
    if sys.platform != 'win32':
        return False
    try:
        import winreg
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r'Software\PythonHelper')
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)
        return True
    except Exception:
        return False


def check_python() -> str:
    """检测 Python 版本，返回版本字符串，失败返回空字符串。"""
    try:
        result = subprocess.run(
            ['python', '--version'],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return '未知'
    except Exception:
        return ''


# ============ 你要写的地方 ============

def main():
    print('python配置小助手')
    yes_or_no = ask('是否检测 Python 环境？','y')
    file_paths = r'D:\Desktop\ai_cli\ALL\config.txt'
    if yes_or_no != 'y':
        print('再见')
        return
    versions = check_python()
    if versions:
        print(f'Python 版本：{versions}')
    else:
        print('Python 未安装或检测失败')
    project_name = ask('请输入项目名称','my_project')
    if project_name:
        if Path(file_paths).exists():
            backup(Path(file_paths))
        write_text(Path(file_paths), f'[project]\nname={project_name}\npython_version = {versions}\n')
        result = save_setting('project_name', project_name)
        if result:
            print('配置完成！')



if __name__ == '__main__':
    main()