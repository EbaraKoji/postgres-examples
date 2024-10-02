import psycopg
from psycopg.rows import dict_row


def safe_search_category(category: str, use_placeholder=True):
    raw_unsafe_query = f"""PREPARE safe_query(varchar(50)) AS SELECT * FROM products WHERE category = $1 AND released = TRUE;
    EXECUTE safe_query('{category}');
    DEALLOCATE safe_query;
    """
    safe_query = (
        'SELECT * FROM products WHERE category = %s AND released = TRUE;'
    )
    with psycopg.connect(
        host='localhost',
        port=5432,
        dbname='postgres',
        user='postgres',
        password='pg_secret',
        row_factory=dict_row,
    ) as conn:
        with conn.cursor() as cur:
            if use_placeholder:
                cur.execute(safe_query, (category,))
            else:
                cur.execute(raw_unsafe_query)
            return cur.fetchall()


category = 'Health'
result = safe_search_category(category)
unreleased_count = len([item for item in result if item['released'] is False])
print(f'[HARMLESS] unreleased_count: {unreleased_count}')

toxic_category = "Health' -- "
result = safe_search_category(toxic_category, use_placeholder=True)
unreleased_count = len([item for item in result if item['released'] is False])
print(f'[TOXIC] unreleased_count: {unreleased_count}')

toxic_category = "Health' -- "
try:
    result = safe_search_category(toxic_category, use_placeholder=False)
except psycopg.ProgrammingError as e:
    print(e)
