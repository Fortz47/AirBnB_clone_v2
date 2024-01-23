#!/usr/bin/python3
"""starts a Flask web application:"""

from models import storage
from flask import Flask, render_template
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """closes sqlalchemy session"""
    storage.close()

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_list(id=None):
    """lists all states along with their cities"""
    states = storage.all('State').values()
    state = None
    for item in states:
        if item.id == id:
            state = item
            break

    return render_template('9-states.html',
                           states=states, state=state, Id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
