from flask import Flask, request

app = Flask(__name__)


@app.route("/xss")
def xss():
    html = '''
	<!DOCTYPE html>
	<html lang="ja">
	<h1>format</h1>
	<h2>input url</h>
	<input type="text" name="id">
	<button type="submit" value=Login><a href="text">login</a></button>

	</html>'''

    return html


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5050)
