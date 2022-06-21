import PySimpleGUI as sg

# 画面レイアウトを指定
layout = [
    [sg.Text('Please input num.')],
    [sg.Text('num:'), sg.InputText(key='st')],
    [sg.Button('exchange')],
    [sg.Text('---', key='info', size=(50, 10))]
]
# ウィンドウの作成
win = sg.Window('squared calculate', layout)

# ウィンドウのイベントループ
while True:
    # イベントにおけるパラメーターの取得
    event, val = win.read()
    # ウィンドウの終了イベント判定
    if event in ('Exit', 'Quit', None):
        break
    # 変換ボタンが押された場合の処理を適宜コーディング
    if event == 'exchange':

        # パラメータを渡す
        num = int(val['st'])
        plain = ""

        plain = num * num

        s = 'Squared:', format(plain)
        # テキストを更新
        win['info'].update(s)

win.close()
