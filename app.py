from flask import Flask, render_template, request
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

@app.route('/offers', methods=['GET', 'POST'])
def offers():
    if request.method == 'GET':
        data = execute_sql(
            "datab",
            """
                SELECT p.name, p.description, s.company_name, t.name, p.image
                FROM product p
                JOIN type_of_product t ON p.type_of_product_id = t.id
                JOIN supplier s ON p.supplier_id = s.id;
            """
        )
        return render_template('offers.html', data=data)
    else:
        data = execute_sql(
            "datab",
            f"""
                SELECT p.name, p.description, s.company_name, t.name, p.image
                FROM product p
                JOIN type_of_product t ON p.type_of_product_id = t.id
                JOIN supplier s ON p.supplier_id = s.id
                WHERE p.name ILIKE '%{request.form['phrase']}%';
            """
        )
        return render_template('offers.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)