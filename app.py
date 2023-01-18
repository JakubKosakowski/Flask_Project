from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/hospital'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
conn = psycopg2.connect(database="hospital", user="postgres", password="password", host="localhost")
mycursor = conn.cursor()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')