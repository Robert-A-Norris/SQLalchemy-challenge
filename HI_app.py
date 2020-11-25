import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base =  automap_base()
Base.prepare(engine,reflect = True)
Station = Base.classes.station 
Measurement = Base.classes.measurement

app = Flask(__name__)




@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<end>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    
    session = Session(engine)

    #Convert the query results to a dictionary using `date` as the key 
    # and `prcp` as the value.
    
    query = session.query(Measurement.date, Measurement.prcp.filter(Measurement.date >=2016-08-23).all()
    
   

    # Return the JSON representation of your dictionary.
    results = list(np.ravel(results))

    return jsonify(results)


@app.route("/api/v1.0/stations")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Return a JSON list of stations from the dataset.
    station_list = session.query(Station.station).all()
    station = list(np.ravel(stations_list))
    return jsonify(station)

@app.route("/api/v1.0/tobs")
def tobs():
#Query the dates and temperature observations of the most active station 
# for the last year of data.
query = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >=2016-08-23)
.all()
#Return a JSON list of temperature observations (TOBS) for the previous year.
return jsonify(query)



@app.route("/api/v1.0/start/end")
def start/end():
#Return a JSON list of the minimum temperature, the average temperature, and the max 
# temperature for a given start or start-end range.

#When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than
# and equal to the start date.

#When given the start and the end date, calculate the `TMIN`, `TAVG`, and 
# `TMAX` for dates between the start and end date inclusive.







session.close()