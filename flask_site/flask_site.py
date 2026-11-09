from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
@app.route("/hello/<user_name>")
def hello(user_name=None):
    return render_template('home.html', user=user_name)