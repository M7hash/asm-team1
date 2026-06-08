from database.db import get_connection

def save_asset(hostname, source):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO assets(hostname, source)
        VALUES(%s, %s)
        ON CONFLICT(hostname)
        DO NOTHING;
        """,
        (hostname, source)
    )

    conn.commit()

    cur.close()
    conn.close()
