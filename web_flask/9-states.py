#!/usr/bin/python3

from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from sqlalchemy.orm import scoped_session, sessionmaker



app = Flask(__name__)

@app.teardown_appcontext
def tear(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State")

    return render_template("7-states_list.html", states=states)
@app.route('/cities_by_states', strict_slashes=False)
def city_by_state():
    states = storage.all("State")
    cities = storage.all("City")

    return render_template("8-cities_by_states.html", states=states, cities=cities)
@app.route('/states', strict_slashes=False)
def states():
    states= storage.all("State")
    cities = storage.all("City")
    return render_template("9-states.html", states=states, cities=cities)

@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    states = storage.all("State")
    cities = storage.all("City")
    return render_template("9-states.html", states=states, cities=cities, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
