#!/usr/bin/python3
"""starts a Flask web application:"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """closes sqlalchemy session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    lists all states along with their cities.
    lists amenities
    lists places

    """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = storage.all('User').values()
    user_dict = {x.id: f'{x.last_name} {x.first_name}' for x in users}

    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           users=user_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
