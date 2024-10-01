SELECT
    first_name,
    date_of_birth,
    AGE (NOW(), date_of_birth) AS age
FROM
    person
LIMIT
    5;