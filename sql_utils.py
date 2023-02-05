from psycopg2 import connect, OperationalError as Error

USER = 'postgres'
PASSWORD = 'password'
HOST = 'localhost'

def execute_sql(db, sql_code, params = None):
    cnx = connect(user=USER, database=db, password=PASSWORD, host=HOST)