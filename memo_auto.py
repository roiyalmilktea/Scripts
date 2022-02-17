import time,subprocess,platform
import pyautogui as pa


if platform.system() == 'Windows':
	subprocess.Popen(r'c:Windows/notepad.exe')