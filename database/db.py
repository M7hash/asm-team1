import psycopg2

def get_connection():

    conn = psycopg2.connect(
        host="localhost",
        database="asm",
        user="postgres",
        password="StrongPassword123"
    )

    return conn
