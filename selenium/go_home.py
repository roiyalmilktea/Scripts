import smtplib
import datetime
from email.mime.text import MIMEText
import ssl
import codecs
from time import sleep
import schedule
import time

# メール設定の情報
smtp_host = 'smtp.gmail.com'
smtp_port = 587

to_mail = 'bl19067@cc.it-hiroshima.ac.jp'
gmail_account = 'userdev744@gmail.com'
gmail_password = 'inkd aoyg kflg hgrv'  # 送信元はChromeの設定からパスワードを取得する


def func():
    mess = str(input('message:'))  # メール本文を作成
    message = mess
    msg = MIMEText(message, 'html')
    sbj = str(input('subject:'))  # 用件を記述
    msg['Subject'] = sbj
    msg['From'] = gmail_account
    msg['To'] = to_mail

  

    # メールサーバへのアクセス
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_account, gmail_password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    func()
    schedule.every().day.at("16:16").do(func)

    while True:
        schedule.run_pending()
        time.sleep(1)
