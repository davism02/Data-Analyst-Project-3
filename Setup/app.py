import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
import pandas as pd
from flask import Flask, jsonify, render_template, redirect

# In[2]:

connection_string = "postgres:postgres@localhost:5432/data_analyst_db"
engine = create_engine(f'postgresql://{connection_string}')
#engine.table_names()
Base=automap_base()
Base.prepare(engine,reflect=True)
Base.classes.keys()

table=Base.classes.data_analyst_testing

# In[3]:
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/lowest")
# def lowest():
#     session=Session(engine)


#     # In[7]:


#     min_by_location=session.query(table.Location,func.sum(table.min)).group_by(table.Location).all()
#     result = []
#     for i in min_by_location:
#         min_by_location_dict = {}
#         min_by_location_dict["city-state"] = i[0]
#         min_by_location_dict["The lowest min"] = i[1]
#         result.append(min_by_location)

#     return jsonify(result)
#     #return render_template("lowest.html",result=result)

@app.route("/data")
def data():
    session=Session(engine)


    # In[7]:


    rows=session.query(table.ID,table.Title,table.Salary,table.Rating,table.Company,table.Headquarters,table.Size,table.ownership,table.Industry,table.Sector,table.Revenue,table.min,table.max).all()
   
    # for i in all_data:
    #     all_data_dict= {}
    #     all_data_dict= i[0]
    #     min_by_location_dict["The lowest min"] = i[1]
    #     result.append(min_by_location)
    data_list=[]
    for row in rows:
        data_list.append(list(row))
   
    return jsonify(data_list)

if __name__ == "__main__":
    app.run(debug=True)