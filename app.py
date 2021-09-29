from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from flask import Flask, render_template, redirect, jsonify

#setup connection to database



connection_string = "postgres:postgres@localhost:5432/data_analyst_db"
engine = create_engine(f'postgresql://{connection_string}')
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
app = Flask(__name__)

#db = sqlalchemy(app)

app.config = "postgres:postgres@localhost:5432/data_analyst_db"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():
    print(Base.classes.keys())
    result = {"success": True, "data": []}
    return jsonify(result)
    
  
if __name__ == "__main__":
    app.run(debug=True)