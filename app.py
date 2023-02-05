from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
conn = psycopg2.connect(database="northwind", user="postgres", password="password", host="localhost")
mycursor = conn.cursor()


@app.route('/')
def home():
    mycursor.execute("SELECT * FROM orders")
    data = mycursor.fetchall()
    return render_template('home.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()