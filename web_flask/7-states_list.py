#!/usr/bin/python3
"""starts a Flask web application:"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """closes sqlalchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """lists all states"""
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
