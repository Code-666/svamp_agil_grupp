from flask import Flask
from flask import render_template, request, flash, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, world and Svampar</p>"


@app.route("/test")
def test():
    return "<p>Hello, Svamp. new endpoint.</p>"


@app.route("/svamp")
def svamp():
    return "<p> Hello, Svampälskare. </p>"


@app.route("/mj_test")
def mj_test():
    """
    ...
    """
    return render_template("mj_test.html")


if __name__ == "__main__":
    app.run(debug=True)
