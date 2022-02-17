import smtplib
import ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail
import datetime
import schedule
import time

# メイン処理


def send_test_email():
    msg = make_mime_text(
        mail_to=gmail.account,
        subject='バイト',
        body='明日バイトあるで！時間確認しとき')
    send_gmail(msg)
# メールデータを生成


def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['To'] = mail_to
    msg['From'] = gmail.account

    return msg

    # Outlookのサーバに接続


def send_gmail(msg):
    # gmailのサーバに接続
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465,
                              context=ssl.create_default_context())
    server.set_debuglevel(1)
    server.login(gmail.account, gmail.password)
    server.send_message(msg)


if __name__ == "__main__":
    schedule.every().tuesday.at("17:09").do(send_test_email())
    schedule.every().saturday.at("17:09").do(send_test_email())
    print('OK')
