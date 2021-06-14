"""Learning URLs"""

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1><em>Hello World!</em></h1>"

@app.route('/dynamic/<int:num>')
def dynamic(num):
    return str(num)

@app.route('/redirecting/<int:score>')
def redirecting(score):
    score = 25
    return redirect(url_for("dynamic", num=score))

if __name__=='__main__':
    app.run(debug=True)