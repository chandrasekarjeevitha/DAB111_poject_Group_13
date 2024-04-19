from flask import Flask, render_template
import sqlite3
from pathlib import Path
import os

base_path = Path().cwd()
db_name = "online_delivery.db"
db_path = base_path / db_name
my_path= os.path.join(os.path.dirname(__file__), db_name)

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(my_path)
    cursor = con.cursor()
    online_orders = cursor.execute("SELECT * FROM online_orders WHERE id IN (SELECT MIN(id) AS id FROM online_orders GROUP BY city)").fetchall()
    con.close()

    return render_template("data_table.html", online_orders=online_orders)

if __name__=="__main__":
    app.run(debug=True)
