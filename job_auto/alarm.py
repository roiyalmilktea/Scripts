import datetime
import schedule
import time
import PySimpleGUI as sg


def alarm_func():
    print(datetime.datetime.now())
    layout = [
        [sg.Text('はよ帰れ！')],
        [sg.OK()],
    ]
    # windowの作成
    win = sg.Window('Alart!', layout)

    while True:
        event, val = win.read()
        if event in ('Exit', 'Quit', None):
            break
        if event == 'OK':
            break
    win.close()


schedule.every().day.at("15:40").do(alarm_func)

while True:
    schedule.run_pending()
    time.sleep(60)
