SELECT
    id,
    first_name,
    last_name
FROM
    person
OFFSET
    5
LIMIT
    5;

-- OFFSET 5 FETCH FIRST 5 ROW ONLY; -- SQL Standard