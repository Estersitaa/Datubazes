import sqlite3
from flask import 

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    skoleni_no_db = iegut_skolenus()
    print(skoleni_no_db)

    if request.method == "POST"
       vards = request.form['name']
       uzvards = request.form
    if 
    if 

dati = f"pievienots skolēns - {vards} {uzvards}, {skolotajs}"

def pievienot_skolotaju(vards, uzvards):
    print(vards, uzvards)

def pievienot_prieksmetu(prieksmerts):
    print()

def iegut_skolotajus():
cur = conn.cursor()
cur.execute()
    """SELECT vards, uzvards FROM skolotaji"""

def skolotaju_tabulas_izveide()
    

conn.commit()
dati = cur.fetcall()
return dati
