import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/goodbye')
def goodbye_world():
    return 'Goodbye world'

@app.route('/one_more')
def one_more_string():
    return 'One more string'