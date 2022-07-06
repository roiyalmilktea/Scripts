from flask import Flask, request

app = Flask(__name__)


@app.route("/xss")
def xss():
    html = '''
	<!DOCTYPE html>
	<html lang="ja">
	<h1>as</h1>
	<input type="text" name="id">
        <button type="submit" value="Login">Login</button>
	
	</html>
	'''
    return html


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
