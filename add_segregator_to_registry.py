import os
import sys
import winreg

cwd = os.getcwd()

python_exe = sys.executable.replace("python", "pythonw")

key_path = r"Directory\\Background\\shell\\Picked image matcher"

key = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, key_path)

winreg.SetValue(key, '', winreg.REG_SZ, "&Separate sorted RAWs")

key1 = winreg.CreateKeyEx(key, r"command")
winreg.SetValue(key1, '', winreg.REG_SZ, python_exe + f' "{cwd}\\picked_image_matcher.pyw"')
