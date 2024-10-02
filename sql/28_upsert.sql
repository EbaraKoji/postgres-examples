SELECT
    *
FROM
    person
WHERE
    id = 1;

INSERT INTO
    person (id, first_name, last_name, email, gender, date_of_birth, country_of_birth) OVERRIDING SYSTEM VALUE
VALUES
    (1, 'Redford', 'Goodbar', 'updated@example.com', NULL, '1960-04-09', 'France') ON CONFLICT (id)
DO
UPDATE
SET
    email = EXCLUDED.email;

SELECT
    *
FROM
    person
WHERE
    id = 1;

UPDATE person
SET
    email = 'rgoodbar0@about.me'
WHERE
    id = 1;

SELECT
    *
FROM
    person
WHERE
    id = 1;