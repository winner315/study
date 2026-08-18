from pathlib import Path
import shutil
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


            # ─── 请你在下面填空 ───
    # 1. 定义日记文件路径：当前目录下的 diary.txt
    # 2. 用 ask 询问用户今天想写什么（提示文字："今天想写什么"）
    #    （默认值可以不传，或传个空字符串，但 ask 的 default 已经有默认值 '' 了）
    # 3. 如果用户输入了内容（非空）：
    #    a. 先备份旧文件（调用 backup）
    #    b. 读取旧内容（调用 read_text）
    #    c. 打印旧内容（如果有的话，打印"历史日记：\n{旧内容}"）
    #    d. 把新内容追加到文件（追加模式用 'a'，加个换行和日期标记）
    #    e. 打印 "日记已保存！"
    # 4. 如果用户没输入内容，打印 "日记未保存。"
    pass  # 删掉这行，写上你的代码


if __name__ == '__main__':
    main()