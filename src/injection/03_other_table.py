from pprint import pprint

import psycopg
from psycopg.rows import dict_row


def dangerous_search_category(category: str):
    unsafe_query = f"SELECT item_name, category FROM products WHERE category = '{category}' AND released = TRUE;"
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


category = 'Health'
result = dangerous_search_category(category)
pprint(result[:5])


toxic_category = "' UNION SELECT username, password FROM users-- "
result = dangerous_search_category(toxic_category)
pprint(result[:5])
