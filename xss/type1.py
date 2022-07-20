import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__)


def get_db():
    if 'db' not in g:
        # データベースをオープンしてFlaskのグローバル変数に保存
        g.db = sqlite3.connect('wordlist.db')
    return g.db


@app.route('/')
def index():

    # データベースを開く
    con = get_db()

    # テーブル「商品一覧」の有無を確認
    cur = con.execute(
        "select count(*) from sqlite_master where TYPE='table' AND name='wordlist'")

    for row in cur:
        if row[0] == 0:
            # テーブル「商品一覧」がなければ作成する
            cur.execute(
                "CREATE TABLE wordlist(code INTEGER PRIMARY KEY, word STRING, mean STRING)")
            # レコードを作る
            cur.execute(
                """INSERT INTO wordlist(code, word, mean) 
                values(1, 'hello', 'コンニチワ'),
                (2, 'goodmorning','オイーッス')
                
                """)
            con.commit()

    # 商品一覧を読み込み
    cur = con.execute("select * from wordlist order by code")

    data = cur.fetchall()
    con.close()

    return render_template('dictionary.html', data=data)


@app.route('/result', methods=["POST"])
def result_post():

    word = request.form["word"]
    mean = request.form["mean"]

    # データベースを開く
    con = get_db()

    # コードは既に登録されているコードの最大値＋１の値で新規登録を行う
    cur = con.execute("select MAX(code) AS max_code from wordlist")
    for row in cur:
        new_code = row[0] + 1
    cur.close()

    # 登録処理
    sql = "INSERT INTO wordlist(code, word, mean)values({},'{}','{}')".format(
        new_code, word, mean)
    con.execute(sql)
    con.commit()

    # 一覧再読み込み
    cur = con.execute("select * from wordlist order by code")
    data = cur.fetchall()
    con.close()

    return render_template('dictionary.html', data=data)


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
