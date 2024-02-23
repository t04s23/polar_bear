import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # open the connection to the database
    conn = sqlite3.connect('polar_bear_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from deployments")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)


@app.route('/<id>')
def deployment(id):
    # open the connection to the database
    conn = sqlite3.connect('polar_bear_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from status WHERE deployment_id="+ id +" AND received<>''" +" AND latitude<>''" +" AND longitude<>''" +" AND temperature<>''")
    rows = cur.fetchall()
    conn.close()
    return render_template('deployment.html', rows=rows)
