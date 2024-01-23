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


@app.route('/cities_by_states', strict_slashes=False)
def state_city_list():
    """lists all states along with their cities"""
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
