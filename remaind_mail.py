import smtplib
import ssl
from email.mime.text import MIMEText
from gmail_send import send_test_email
import my_gmail_account as gmail
import time


def send_test_email():
    msg = make_mime_text(
        mail_to=gmail.account,
        subject='リマインド',
        body='なんかあるからカレンダー確認しな！')
    send_gmail(msg)


def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['To'] = mail_to
    msg['From'] = gmail.account

    return msg


def send_gmail(msg):
    server = smtplib.SMTP_SSL(
        'smtp.gmail.com', 465,
        context=ssl.create_default_context())
    server.set_debuglevel(0)  # ログ出力
    # ログインしてメールを送信
    server.login(gmail.account, gmail.password)
    server.send_message(msg)


if __name__ == '___main__':
    send_test_email()
    print('ok')
