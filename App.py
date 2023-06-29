from flask import Flask, render_template, request, redirect, session 
import sqlite3
import os
import dotenv

dotenv.load_dotenv('.env', encoding='latin-1')

conn = sqlite3.connect('offaly.db') 
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(24)

#cursor = conn.execute('SELECT * FROM registrants')
#rows = cursor.fetchall()
#print(rows)
#print(os.environ)

@app.route("/")

def index():

    return render_template("index.html")