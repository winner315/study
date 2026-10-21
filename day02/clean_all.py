import sys
import ctypes
from pathlib import Path
import shutil


def clean_all():
    """清理练习产生的所有垃圾数据。"""

    # 1. 清理注册表
    if sys.platform == 'win32':
        try:
            import winreg
            # 删除 PythonHelper
            try:
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r'Software\PythonHelper')
                print('✅ 已删除注册表：PythonHelper')
            except FileNotFoundError:
                print('ℹ️  PythonHelper 不存在，跳过')
            # 删除 MyApp
            try:
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r'Software\MyApp')
                print('✅ 已删除注册表：MyApp')
            except FileNotFoundError:
                print('ℹ️  MyApp 不存在，跳过')
            # 删除 MyAppSettings
            try:
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r'Software\MyAppSettings')
                print('✅ 已删除注册表：MyAppSettings')
            except FileNotFoundError:
                print('ℹ️  MyAppSettings 不存在，跳过')
        except Exception as e:
            print(f'注册表清理出错：{e}')

    # 2. 清理练习文件
    files_to_delete = [
        Path('settings.txt'),
        Path('memo.txt'),
        Path('config.txt'),
        Path('diary.txt'),
        Path(r'D:\Desktop\ai_cli\ALL\config.txt'),
    ]
    for f in files_to_delete:
        if f.exists():
            f.unlink()
            print(f'✅ 已删除文件：{f}')
        else:
            print(f'ℹ️  文件不存在，跳过：{f}')

    # 3. 清理备份文件（.bak 结尾的）
    for f in Path('.').glob('*.bak*'):
        f.unlink()
        print(f'✅ 已删除备份：{f}')

    print('\n🎉 清理完成！环境已恢复原样。')


if __name__ == '__main__':
    clean_all()