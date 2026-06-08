import psycopg2

def get_connection():

    conn = psycopg2.connect(
        host="localhost",
        database="asm",
        user="postgres",
        password="postgrespass"
    )

    return conn
