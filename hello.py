from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<name>")
def index1(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == "__main__":
    manager.run()