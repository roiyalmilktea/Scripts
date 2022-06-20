import PySimpleGUI as sg

# 画面レイアウトを指定
layout = [
    [sg.Text('Do you know rot13?')],
    [sg.Text('string'), sg.InputText(key='st')],
    [sg.Button('exchange')],
    [sg.Text('---', key='info', size=(50, 10))]
]
# ウィンドウの作成
win = sg.Window('seaser cryptography', layout)

# ウィンドウのイベントループ
while True:
    # イベントにおけるパラメーターの取得
    event, val = win.read()
    # ウィンドウの終了イベント判定
    if event in ('Exit', 'Quit', None):
        break
    # 変換ボタンが押された場合の処理を適宜コーディング
    if event == 'exchange':

        strings = str(val['st'])  # パラメータを渡す
        plain = ""
        for char in list(strings):
            ASCII = ord(char)
            num = ASCII - 97
            num = (num - 13) % 26
            ASCII = num + 97
            plain += chr(ASCII)

        s = 'decrypto:', format(plain)
        # テキストを更新
        win['info'].update(s)

win.close()
