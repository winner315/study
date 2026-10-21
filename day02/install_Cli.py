import subprocess
from asyncio import timeout


def install_Cli(npm_cmd:str,package_name:str,label:str) ->bool:
    print(f'正在安装{label}({package_name})...')
    print(f'命令"{npm_cmd}" install -g {package_name}')
    try:
        result = subprocess.run([npm_cmd,'install','-g',package_name],timeout=300)
        if result.returncode == 0:
            print(f'√{label}安装完成')
            return True
        else:
            print(f'√{label}安装失败，报错原因{result.returncode}')
            return False
    except FileNotFoundError:
        print(f'找不到npm_cmd{npm_cmd},请确认 Node.js 已正确安装。')
        return False
    except subprocess.TimeoutExpired:
        print(f'✗ {label} 安装超时（超过 5 分钟），请检查网络后重试。')
        return False
    except Exception as e:
        print(f'✗ 安装出错: {e}')
        return False