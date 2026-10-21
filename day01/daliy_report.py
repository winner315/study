import shutil
from pathlib import Path
import shutil_study
import datetime


def ask(prompt: str, default: str = '') -> str:
    """交互式输入，支持默认值。"""
    if default:
        prompt = f'{prompt}（默认 {default}）：'
    else:
        prompt = f'{prompt}：'
    v = input(prompt).strip()
    return v if v else default


def read_text(filepath: Path) -> str:
    """读取文件内容，不存在返回空字符串。"""
    if not filepath.exists():
        return ''
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def backup(filepath: Path):
    """备份文件为 .bak-{时间戳} 格式。"""
    if not filepath.exists():
        return "文件不存在，跳过备份"
    else:
        hz = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        bak = filepath.with_suffix(f'{filepath.suffix}-{hz}.bak')
        shutil.copy2(filepath,bak)
        return  f"已备份为：{bak}"



def main():
    filepath = Path('diary.txt').resolve()
    content = ask("今天想写什么")
    if content:
        backup(filepath)
        file_content = read_text(filepath)
        if len(file_content)>0:
            print(f"历史日记：\n{file_content}")
        with open('diary.txt', 'a', encoding='utf-8') as f:
            dates = datetime.datetime.today().strftime('%Y年%m月%d日')
            write_content = f'{dates}\n{content}\n'
            f.write(write_content)
            print(f'日记保存成功\n{write_content}\n')
    else:
        print('日记为保存')

if __name__ == '__main__':
    main()