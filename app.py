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
    tea_type = execute_sql(
        "datab",
        """
            SELECT name
            FROM type_of_product;
        """
    )
    if request.method == 'GET':
        data = execute_sql(
            "datab",
            """
                SELECT p.id, p.name, p.description, p.image, p.unit_price
                FROM product p
                JOIN type_of_product t ON p.type_of_product_id = t.id
                JOIN supplier s ON p.supplier_id = s.id;
            """
        )
        return render_template('offers.html', data=data, tea_type=tea_type)
    else:
        flag = True
        sql_code = f"""
                    SELECT p.id, p.name, p.description, p.image, p.unit_price
                    FROM product p
                    JOIN type_of_product t ON p.type_of_product_id = t.id
                    JOIN supplier s ON p.supplier_id = s.id
                    WHERE """
        if request.form.get('phrase') != '':
            flag = False
            sql_code += f"""p.name ILIKE '%{request.form['phrase']}%' AND """
        if request.form['price_min']:
            flag = False
            sql_code += f"""p.unit_price > {request.form['price_min']} AND """
        if request.form['price_max']:
            flag = False
            sql_code += f"""p.unit_price < {request.form['price_max']} AND """
        for tea in tea_type:
            if request.form.get(f'{tea[0]}'):
                flag = False
                sql_code += f"""t.name = '{tea[0]}' OR """
        if not flag:
            sql_code = sql_code[:-4] + """;"""
        else:
            sql_code = sql_code[:-6] + """;"""

        data = execute_sql(
                "datab",
                sql_code
        )

        return render_template('offers.html', data=data, tea_type=tea_type)


@app.route('/product_details/<int:id>')
def product_details(id):
    details = execute_sql(
        "datab",
        """
            SELECT
                p.name
                , p.description
                , p.medical_properties
                , p.unit_price
                , p.quentity_per_unit
                , s.company_name
                , t.name
                , t.brewing_time
                , t.brewing_temperature
                , t.amount_per_cup
            FROM product p
            JOIN type_of_product t ON p.type_of_product_id = t.id
            JOIN supplier s ON p.supplier_id = s.id
            WHERE p.id = %s
        """,
        (id,)
    )
    return render_template('product_details.html', details=details)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)