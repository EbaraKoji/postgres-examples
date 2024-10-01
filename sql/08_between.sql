SELECT
    id,
    first_name,
    date_of_birth
FROM
    person
WHERE
    date_of_birth BETWEEN DATE '2000-01-01' AND '2015-12-31'
LIMIT
    10;