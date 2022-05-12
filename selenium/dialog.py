import tkinter.messagebox as mb
import tkinter as tk
import time


tk.Tk().withdraw()

# 二択ダイアログを表示
yesno = mb.askyesno('alart!', 'check schedule')

# ユーザの回答により動作を変更
if yesno:
    mb.showinfo('Yes', 'done')

else:
    mb.showinfo('No', 'not done')
