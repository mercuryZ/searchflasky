from flask import Flask, render_template
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route("/")
def index():
    return render_template('index.html')


# @app.route("/<name>")
# def index1(name):
#     return '<h1>Hello, %s!</h1>' % name


@app.route("/<int:num>")
def index2(num):
    return '<h1>Hello, %s!</h1>' % str(num)


if __name__ == "__main__":
    manager.run()