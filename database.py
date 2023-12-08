import psycopg2

conn_params = {
    'dbname': 'Flask2',
    'user': 'postgres',
    'password': 'idontknow4',
    'host': 'localhost'
}

def get_db_connection():
    return psycopg2.connect(**conn_params)
