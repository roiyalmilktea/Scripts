from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('test.db')
    return g.db


@app.route('/')
def index():
    con = get_db()


##########################################################

db_name = 'samplelist.db'
conn = sqlite3.connect(db_name)

cursor = conn.cursor()
conn.commit()
cur = conn.execute("SELECT * FROM product")
for row in cur:
    print(row)
    print(type(row))
cur.close()


@route('/')
def hello(user=''):
    tasks = get_samplelist()

    html = '''

    '''
    return html


@route('/', method='POST')
def register():
    name = request.forms.get('name')
    detail = request.forms.get('detail')

    sql_query = 'INSERT INTO samplelist values(?, ?)'
    cursor.execute(sql_query, (name, detail))
    conn.commit()

    return redirect('/')


def get_samplelist():
    sql_query = 'SELECT * FROM samplelist'
    result = cursor.execute(sql_query)

    html = '<table border="1">'
    for row in result:
        html += '<tr><td>'
        html += row[0]
        html += '</td><td>'
        html += row[1]
        html += '</td></tr>'

    html += '</table>'
    return html


run(host='localhost', port=5000, debug=True)
