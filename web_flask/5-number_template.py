"""script that starts a Flask web application"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """returns a text"""
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text='is cool'):
    """returns a text"""
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """displays <n> is a number only in n is int"""
    return f'{escape(n)} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_number_template(n):
    """displays a HTML page only in n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
