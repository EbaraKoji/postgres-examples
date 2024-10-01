SELECT
    id,
    first_name,
    email
FROM
    person
WHERE
    email LIKE '%.org'
    OR email LIKE '%.jp'
LIMIT
    5;

SELECT
    id,
    first_name,
    email
FROM
    person
WHERE
    email LIKE '%@google.%' -- contains '@google.'
LIMIT
    5;

SELECT
    id,
    first_name,
    email
FROM
    person
WHERE
    email LIKE '_______k@%';

-- 7 characters + 'k'