import sys
import ctypes

def save_setting(name: str, value: str) -> bool:
    if sys.platform != 'win32':
        print('仅支持Windows')
        return False
    try:
        import winreg
        key =winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                       r'Software\MyApp')
        winreg.SetValueEx(key,name,0,winreg.REG_SZ,value)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f'保存失败：{e}')
        return False

def delete_setting(name: str, value: str) -> bool:
    if sys.platform != 'win32':
        print('仅支持Windows')
        return False
    try:
        import winreg
        key =winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                       r'Software\MyApp',
                            0,
                            winreg.KEY_SET_VALUE|winreg.KEY_QUERY_VALUE)
        winreg.DeleteValue(key, name)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f'保存失败：{e}')
        return False

# 测试
# save_setting('theme', 'dark')
# delete_setting('language', 'zh-CN')