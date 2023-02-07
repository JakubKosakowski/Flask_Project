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
                SELECT p.name, p.description, p.image, p.unit_price
                FROM product p
                JOIN type_of_product t ON p.type_of_product_id = t.id
                JOIN supplier s ON p.supplier_id = s.id;
            """
        )
        tea_type = execute_sql(
            "datab",
            """
                SELECT name
                FROM type_of_product;
            """
        )
        return render_template('offers.html', data=data, tea_type=tea_type)
    else:
        tea_type = execute_sql(
            "datab",
            """
                SELECT name
                FROM type_of_product;
            """
        )
        if request.form['phrase'] != '':
            data = execute_sql(
                "datab",
                f"""
                    SELECT p.name, p.description, p.image, p.unit_price
                    FROM product p
                    JOIN type_of_product t ON p.type_of_product_id = t.id
                    JOIN supplier s ON p.supplier_id = s.id
                    WHERE p.name ILIKE '%{request.form['phrase']}%';
                """
            )
        else:
            sql_code = f"""
                    SELECT p.name, p.description, p.image, p.unit_price
                    FROM product p
                    JOIN type_of_product t ON p.type_of_product_id = t.id
                    JOIN supplier s ON p.supplier_id = s.id
                    WHERE """
            for tea in tea_type:
                if request.form.get(f'{tea[0]}'):
                    sql_code += f"""t.name = '{tea[0]}' OR """
            sql_code = sql_code[:-4] + """;"""
            data = execute_sql(
                "datab",
                sql_code
            )

        return render_template('offers.html', data=data, tea_type=tea_type)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)