import psycopg
from uuid import uuid4

with psycopg.connect(
    host='localhost',
    port=5432,
    dbname='postgres',
    user='postgres',
    password='pg_secret',
    cursor_factory=psycopg.ClientCursor,  # https://stackoverflow.com/questions/78410960/psycopg3-mogrify-attributeerror-connection-object-has-no-attribute-mogrify
) as conn:
    with conn.cursor() as cur:
        print(cur.execute("select gen_random_uuid()").fetchone()[0])
        print(cur.execute("select gen_random_uuid() = %s", [uuid4()]).fetchone()[0])
