from flask import Flask

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