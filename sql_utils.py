from psycopg2 import connect, Error

USER = 'postgres'
PASSWORD = 'password'
HOST = 'localhost'

def execute_sql(db, sql_code, params = None):
    cnx = connect(user=USER, database=db, password=PASSWORD, host=HOST)
    try:
        with cnx.cursor() as cur:
            cur.execute(sql_code, params)
            try:
                res = cur.fetchall()
            except Error:
                res = []
            cnx.commit()
            return res
    finally:
        cnx.close()