#!/usr/bin/python3
"""starts a Flask web application:"""

from models import storage
from flask import Flask

app = Flask(__name__)

@app.teardown_appcontext()
def teardown():
    """closes sqlalchemy session"""
    storage.close()
