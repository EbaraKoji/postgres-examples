SELECT
    id,
    first_name,
    email
FROM
    person
WHERE
    id = 1;

UPDATE person
SET
    first_name = 'Updated user',
    email = 'updated@example.com'
WHERE
    id = 1;

SELECT
    id,
    first_name,
    email
FROM
    person
WHERE
    id = 1;

UPDATE person
SET
    first_name = 'Redford',
    email = 'rgoodbar0@about.me'
WHERE
    id = 1;

SELECT
    id,
    first_name,
    email
FROM
    person
WHERE
    id = 1;