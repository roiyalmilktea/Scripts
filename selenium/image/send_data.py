from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import datetime
import os
from email.mime.text import MIMEText
import codecs
from time import sleep
import time
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

# メール設定の情報
smtp_host = 'smtp.gmail.com'
smtp_port = 587

to_mail = '4prokouki0526@gmail.com'
gmail_account = 'userdev744@gmail.com'
gmail_password = 'inkd aoyg kflg hgrv'  # 送信元はChromeの設定からパスワードを取得する

# メイン処理


def func():
    mess = str(input('message:'))  # メール本文を作成
    message = mess
    msg = MIMEMultipart()
    sbj = str(input('subject:'))  # 用件を記述
    msg['Subject'] = sbj
    msg['From'] = gmail_account
    msg['To'] = to_mail

    txt = MIMEText('python')
    msg.attach(txt)

    file = str(input('What is name of data you will send?:'))
    # 添付ファイルのディレクトリを指定
    filepath = "/Users/user/Downloads/" + file
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        md = MIMEImage(f.read())
        md.add_header("Content-Disposition", "attachment", filename=filename)
        msg.attach(md)

    # メールサーバへのアクセス
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_account, gmail_password)
    server.send_message(msg)
    server.quit()


# メイン処理実行
if __name__ == '__main__':
    func()
