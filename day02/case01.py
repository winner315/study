import subprocess

def install_package(tool_path: str, package_name: str, label: str) -> bool:
    print(f'正在安装{label}')
    try:
        result = subprocess.run([tool_path,'install',package_name],timeout = 60)
        if result.returncode ==0:
            print(f'{label}安装成功')
            return True
        else:
            print(f'安装失败，退出码{result.returncode}')
            return False
    except FileNotFoundError:
        print(f'{tool_path}未找到')
        return False
    except subprocess.TimeoutExpired:
        print('安装超时')
        return False
    except Exception as e :
        print(f'安装出错，{e}')




# 测试调用（你的代码写好后，取消下面的注释来测试）
print('测试 1：正常安装')
result = install_package('pip', 'requests', '网络请求库')
print(f'结果: {result}\n')