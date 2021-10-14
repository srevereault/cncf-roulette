import csv
import random
from flask import Flask
from flask import render_template

app = Flask(__name__)

with open("cncf.csv", newline="") as file:
    reader = csv.reader(file, delimiter=",", quotechar='"')
    rows = list(reader)

@app.route('/')
def index():
    alea = random.randint(1,761)
    roulette = {'name':rows[alea][0], 'logo':rows[alea][3], 'site':rows[alea][2]}
    return render_template("index.html",roulette=roulette)

