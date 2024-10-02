# Postgres Examples

PostgreSQL example codes with Python.

## Setup

Using docker container, you can instantly set up PostgreSQL and pgadmin4.
```
docker compose up
```

To setup Python environment, install dependencies with [Rye](https://rye.astral.sh/).
```
rye sync 
```

This project uses [psycopg3](https://www.psycopg.org/psycopg3/docs/) as PostgreSQL adapter for Python.


To execute sql files, run `\i <SQL_FILE>` command in the postgres container.
```
docker compose exec -it postgres psql -U postgres
psql (15.2)
Type "help" for help.

postgres=# \i sql/00_create_database.sql
```
