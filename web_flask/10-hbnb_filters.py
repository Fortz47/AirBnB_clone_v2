#!/usr/bin/python3
"""starts a Flask web application:"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """closes sqlalchemy session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """lists all states along with their cities. lists amenities also"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()

    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
