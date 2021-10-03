import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
import pandas as pd
from flask import Flask, jsonify, render_template, redirect

# In[2]:

connection_string = "postgres:xxxxxxx@localhost:5432/da_job"
engine = create_engine(f'postgresql://{connection_string}')
#engine.table_names()
Base=automap_base()
Base.prepare(engine,reflect=True)
Base.classes.keys()

table=Base.classes.data_analyst

# In[3]:
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lowest")
def lowest():
    session=Session(engine)


    # In[7]:


    min_by_location=session.query(table.Location,func.sum(table.min)).group_by(table.Location).all()
    result = []
    for i in min_by_location:
        min_by_location_dict = {}
        min_by_location_dict["city-state"] = i[0]
        min_by_location_dict["The lowest min"] = i[1]
        result.append(min_by_location)

    return jsonify(result)
    #return render_template("lowest.html",result=result)

if __name__ == "__main__":
    app.run(debug=True)