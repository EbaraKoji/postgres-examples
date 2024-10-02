import psycopg
from psycopg.rows import dict_row


def dangerous_search_category(category: str):
    unsafe_query = f"SELECT * FROM products WHERE category = '{category}' AND released = TRUE;"
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
unreleased_count = len([item for item in result if item['released'] is False])
print(f'[HARMLESS] unreleased_count: {unreleased_count}')


toxic_category = "Health' -- "
result = dangerous_search_category(toxic_category)
unreleased_count = len([item for item in result if item['released'] is False])
print(f'[DANGEROUS] unreleased_count: {unreleased_count}')
