from flask import Flask
from jinja2 import Template
from station_time import get_stops, get_arrival_times

app = Flask(__name__)

@app.route("/")
def index():
    with open("templates/index.html", 'r') as file:
        template = Template(file.read())
    
    return template.render()

@app.route("/data/")
def data():
    arrivals = get_arrival_times(get_stops())

    return arrivals[:15]