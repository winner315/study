# Python 学习笔记 —— Day01

> 复习用笔记。基于本目录下所有练习文件整理，涵盖输入输出、字符串、文件读写、路径操作、时间处理、函数定义与备份逻辑等核心知识点。

---

## 目录文件清单

| 文件 | 作用 |
| --- | --- |
| `beiwanglu.py` | 备忘录小助手（写/看备忘录，带日期，追加写入） |
| `daliy_report.py` | 日记工具（先备份旧文件 → 再追加新内容，含历史日记回显） |
| `shutil_study.py` | 配置文件修改器（键=值 格式更新、自动备份），另有 npm 路径查找（被注释） |
| `test.py` | 交互式读取文件并打印（含字符串去引号处理） |
| `main.py` | PyCharm 新建项目的默认模板脚本 |
| `python_lessons.py` | 空文件（预留，尚未填写内容） |
| `diary.txt` | 日记数据文件（示例内容为 2026 年 8 月 18 日） |
| `memo.txt` | 备忘录数据文件（示例：`[2026-08-24] 今天是个好日子！`） |
| `settings.txt` | 配置文件（示例：`theme=light`、`language=zh-CN`） |

---

## 一、基础输入输出

### `input()` 交互式输入
```python
v = input(prompt).strip()   # 读入字符串并去掉首尾空白
```

### 自定义 `ask()` —— 带默认值的输入
`beiwanglu.py` / `daliy_report.py` / `test.py` 中反复出现的模式：
```python
def ask(prompt: str, default: str = '') -> str:
    """交互式输入，支持默认值。"""
    if default:
        prompt = f'{prompt}（默认 {default}）：'
    else:
        prompt = f'{prompt}：'
    v = input(prompt).strip()
    return v if v else default   # 输入为空则返回默认值
```

**`test.py` 的增强版**：还能自动去掉用户输入内容首尾的成对引号（`"abc"` → `abc`）。
```python
if len(v) >= 2:
    if (v.startswith('"') and v.endswith('"')) or \
            (v.startswith("'") and v.endswith("'")):
        v = v[1:-1]          # 去掉首尾引号
```

---

## 二、f-string 字符串格式化

`test.py` 顶部注释中的示例：
```python
name = "小明"
score = 95.5
print(f"姓名：{name},分数:{score}")   # 用 {} 嵌入变量
```

```python
print(f'Hi, {name}')                 # main.py 中示例
```

---

## 三、字符串常用操作

> 注意：Python 字符串是不可变的，这些方法都返回**新字符串**，不修改原字符串。

### 去除空白
```python
text = "  Hello, Python 世界！  "
text.strip()    # 去掉两端空白 → "Hello, Python 世界！"
text.lstrip()   # 去掉左端空白
text.rstrip()   # 去掉右端空白
```

### split 拆分 & join 拼接
```python
a = "apple,banana,orange".split(",")   # → ['apple', 'banana', 'orange']
b = " | ".join(['a', 'b', 'c'])        # → 'a | b | c'
```

---

## 四、文件读写

### 读取文件（存在才读，否则返回空串）
```python
def read_text(filepath: Path) -> str:
    if not filepath.exists():        # 先用 exists() 判断
        return ''
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
```

### 追加写入（带日期标记）
```python
today = datetime.date.today().strftime('%Y-%m-%d')
with open(MEMO_FILE, 'a', encoding='utf-8') as f:
    f.write(f'[{today}] {content}\n')     # 追加模式 'a'
```

### 覆盖写入（自动创建父目录）
`shutil_study.py` 中的写法：
```python
def write_text(filepath: Path, content: str) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)  # 创建父目录，已存在不报错
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
```

### 编码注意
- 中文文本推荐 `encoding='utf-8'`。
- `test.py` 使用了 `utf-8-sig`：这是**带 BOM（字节序标记）的 UTF-8**，读取带 BOM 的文件（如某些记事本/Excel 生成的 UTF-8 文件）时能自动去掉 `﻿` 标记。

---

## 五、pathlib 路径操作

`from pathlib import Path` —— 比字符串路径更优雅、跨平台。

### 常见用法
```python
Path('diary.txt').resolve()          # 解析为绝对路径
filepath.exists()                    # 判断是否存在
filepath.with_suffix('.bak')         # 替换/修改文件扩展名
filepath.parent                      # 上一级目录
filepath.parent.mkdir()              # 创建目录
```

### 拼接路径（用 `/` 运算符）
```python
HOME = Path.home()                   # 用户主目录
NODE_INSTALL_DIR = HOME / '.codex' / 'node'   # 跨平台路径拼接
local_npm = NODE_INSTALL_DIR / 'npm.cmd'
```

---

## 六、datetime 日期时间处理

### 取日期（到天）
```python
datetime.date.today().strftime('%Y-%m-%d')    # → 2026-08-24
```

### 取完整时间戳（到秒，常用于备份命名）
```python
datetime.datetime.now().strftime('%Y%m%d-%H%M%S')   # → 20260824-143050
datetime.datetime.now().strftime('%Y年%m月%d日')     # 中文格式 → 2026年08月24日
```

### 常用格式代码
| 代码 | 含义 |
| --- | --- |
| `%Y` | 4位年份 |
| `%m` | 2位月份 |
| `%d` | 2位日期 |
| `%H` | 24小时制小时 |
| `%M` | 分钟 |
| `%S` | 秒 |

---

## 七、文件备份逻辑（shutil.copy2）

多个脚本都用到的模式：**写文件前先备份，用时间戳区分**。

```python
from typing import Optional
import shutil

def backup(filepath: Path) -> Optional[Path]:
    if filepath.exists():
        ts = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        bak = filepath.with_suffix(f'{filepath.suffix}.bak-{ts}')
        shutil.copy2(filepath, bak)     # copy2 保留文件元数据（时间戳等）
        return bak
    return None
```

**要点：**
- `shutil.copy2`：复制文件并保留元数据（修改时间等）。
- 用时间戳给备份文件命名，避免同名覆盖。

---

## 八、函数定义与类型注解

```python
def ask(prompt: str, default: str = '') -> str:
```
- `: str` 提示参数类型（`Optional[Path]` 表示参数可以是 `None` 或 `Path`）。
- `-> str` 提示返回值类型。
- **类型注解只是提示，Python 运行时并不强制。**

---

## 九、入口判断

```python
if __name__ == '__main__':
    main()
```
- 只有**直接运行**该脚本时才执行 `main()`。
- 作为模块被 `import` 时不执行 → 便于复用。

---

## 十、配置文件（键值对）读取与更新

`shutil_study.py` 的核心逻辑 —— `xx=值` 一行一行的配置文件：

### 读取
```python
lines = file_content.split('\n')      # 每行一个配置
```

### 更新某一个键（有则替换，无则追加）
```python
found = False
for line in lines:
    if line.startswith(key + '='):    # 找到对应键 → 覆盖
        new_lines.append(f'{key}={value}')
        found = True
    else:
        new_lines.append(line)        # 其余原样保留
if not found:                          # 没找到 → 追加新键
    new_lines.append(f'{key}={value}')
new_content = '\n'.join(new_lines)     # 再拼回成字符串
```
> 顺序：先备份 → 再写回文件，保证修改可回退。

---

## 十一、模块导入与 `typing.Optional`

```python
import datetime
import shutil
import shutil_study            # 导入自己写的另一个脚本
from pathlib import Path
from typing import Optional
```

> `import shutil_study` 很有用：文件之间可以互相复用函数（backup、read_text、ask 等被多个脚本共用）。

---

## 十二、常见坑点（务必注意）

### 1. `test.py` 存在 Bug —— 变量名写错
```python
def read_text(filepath: Path) -> Optional[str]:
    if not filepath.exists():
        return ''
    with open(filepaths, 'r', encoding='utf-8-sig') as f:   # ❌ filepaths 拼错
        return f.read()
```
> `filepath`（参数）误写成 `filepaths`（外层变量）。调用时若传入的 `filepaths` 恰好存在会碰巧运行，但**不指向本参数**，一旦二者不一致即为隐患。复习时建议改成 `filepath`。

### 2. `backup()` 在 `shutil_study.py` 中备份调用打印异常
```python
if bak:
     print(f'已备份{bak}')      # 模板被错误缩进（4 空格），会提前终止块
```
> 缩进错误是 Python 最常见错误之一，务必保持统一（一致用 4 空格）。

### 3. `daliy_report.py` 末尾有注释任务 & `main()` 未实现（`pass`）
> 这是一个**填空题**脚本：注释详细描述了要求，`pass` 处等待补全。复习时可作为动手练习题。

### 4. 追加 `(append)` 不会清空旧内容，但**覆盖 `(write)` 会清空**
> 计划好每次用哪种模式，避免误删数据。

---

## 复习自测清单

1. `input()` + `.strip()` 的作用？自定义默认值函数如何写？
2. f-string 怎么插入变量？
3. `strip / lstrip / rstrip / split / join` 各自返回什么？
4. `open()` 三个模式：读、追加、写 用什么字符？
5. 中文文件推荐什么编码？`utf-8-sig` 多带了什么？
6. `Path` 怎么拼接路径、改扩展名、取绝对路径？
7. `datetime` 怎么取年/月/日/时分秒格式化？
8. `shutil.copy2` 和 `copy` 区别？
9. 类型注解 `-> Optional[str]` 是强制还是提示？
10. `if __name__ == '__main__'` 的作用？
11. 配置文件键值对如何"存在就替换、不存在就追加"？（列表 split/append/join）
12. 脚本之间如何互相 `import` 复用函数？
13. 写出 `test.py` 里那个 bug，避免重犯？