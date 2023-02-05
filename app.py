from flask import Flask, render_template
from sql_utils import execute_sql

app = Flask(__name__)

@app.route('/')
def home():
    data = execute_sql(
        "datab",
        """
            SELECT company_name, address, email
            FROM supplier;
        """
    )
    return render_template('home.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()