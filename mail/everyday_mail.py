import requests
import smtplib
import ssl
import schedule
from email.mime.text import MIMEText
import time
from time import sleep


# メール設定
account = '4prokouki0526@gmail.com'  # 送信元
password = ''  # パスワードを取得

address = str(input('to:'))
to_mail = address

smtp_host = 'smtp.gmail.com'
smtp_port = 587


def func():
    mess = str(input('message:'))  # メール本文を作成
    message = mess
    msg = MIMEText(message, 'html')
    sbj = str(input('subject:'))  # 用件を記述
    msg['Subject'] = sbj
    msg['From'] = account
    msg['To'] = to_mail

    # メールサーバへのアクセス
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(account, password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    func()
