import psycopg
from psycopg.rows import dict_row


def dangerous_get_user(username: str, password: str):
    unsafe_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"
    with psycopg.connect(
        host='localhost',
        port=5432,
        dbname='postgres',
        user='postgres',
        password='pg_secret',
        row_factory=dict_row,
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(unsafe_query)
            return cur.fetchall()


username = 'ebarakoji'
password = 'aH8)m"2TH(y'
results = dangerous_get_user(username, password)
print(results)  # get user using right password

results = dangerous_get_user(username, '')
print(results)  # no user without password

toxic_username = "ebarakoji' -- "
results = dangerous_get_user(toxic_username, '')
print(results)  # XXX: get user WITHOUT password!!
