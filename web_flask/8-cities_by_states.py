#!/usr/bin/python3
"""minimal flask app"""

from flask import Flask, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def closedb(foo):
    """Closes db session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """Route /cities_by_states"""
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
