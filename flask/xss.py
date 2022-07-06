from flask import Flask, request
import requests


app = Flask(__name__)


@app.route('/')
def route(user=''):
    username = requests.query.get('user')
    username = '' if username is None else username

    html = '''
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <title>脆弱性</title>
        <meta charset="utf-8"/>
    </head>
    <body>
        <h1>Webアプリケーション攻撃手法</h1>
        <ul>
            <li>web</li>
            add<br>
            <a href="http://localhost:8000/hello/xss">url</a>
            </body>
    </html>'''

    return html


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
