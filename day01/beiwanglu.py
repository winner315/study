from pathlib import Path
import datetime

MEMO_FILE = Path('memo.txt')

def ask(prompt:str,default:str=None) -> str:
    if default:
        prompt = f'{prompt}（默认{default}):'
    else:
        prompt = f'{prompt}:'
    v= input(prompt).strip()
    return v if v else default

def read_text(filepath: Path) -> str:
    if not filepath.exists():
        return ''
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_memo(content: str) -> None:
    """把内容追加到备忘录（带日期）。"""
    with open(MEMO_FILE, 'a', encoding='utf-8') as f:
        today = datetime.date.today().strftime('%Y-%m-%d')
        f.write(f'[{today}] {content}\n')
    print('备忘录已保存！')


def show_memo() -> None:
    """显示所有备忘录内容。"""
    content = read_text(MEMO_FILE)
    if content:
        print('=' * 40)
        print(content)
        print('=' * 40)
    else:
        print('备忘录是空的。')


def main():
    print('='*60+'备忘录小助手'+'='*60)
    print('1-写备忘录 2-查看备忘录 3-退出')
    ch = ask('请选择菜单','3')
    if ch == '1':
        content = ask('请输入内容','')
        if not content:
            print('输入内容不能为空')
        else:
            write_memo(content)
    elif ch == '2':
        show_memo()
    elif ch == '3':
        print('再见')
        return
    else:
        print('无效选择')
        return



if __name__ == '__main__':
    main()