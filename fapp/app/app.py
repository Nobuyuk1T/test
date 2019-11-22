#coding:utf-8

from flask import Flask,render_template

#フラスクオブジェクトの生成
app = Flask(__name__)

#[/]にアクセスがあった場合に文字列を返す
@app.route('/')
def hello():
	return "hello world"

#[/index]へアクセスがあった場合に、[index.html]を返す
@app.route('/index')
def index():
	return render_template('index.html')

if __name__=="__main__":
	app.run(debug=True)
