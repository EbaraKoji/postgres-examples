SELECT
    email,
    COUNT(*)
FROM
    person
GROUP BY
    email
    -- HAVING
    --     COUNT(*) > 1;
ORDER BY
    COUNT(*) DESC
LIMIT
    5;

INSERT INTO
    person (first_name, last_name, email, gender, date_of_birth, country_of_birth)
VALUES
    ('Fernanda', 'Goodbar', 'rgoodbar0@about.me', 'Non-binary', '1960-04-09', 'France');

SELECT
    email,
    COUNT(*)
FROM
    person
GROUP BY
    email
HAVING
    COUNT(*) > 1;

ALTER TABLE person
ADD CONSTRAINT unique_email_address UNIQUE (email);

DELETE FROM person
WHERE
    first_name = 'Fernanda'
    AND email = 'rgoodbar0@about.me';

ALTER TABLE person
ADD CONSTRAINT unique_email_address UNIQUE (email);

INSERT INTO
    person (first_name, last_name, email, gender, date_of_birth, country_of_birth)
VALUES
    ('Fernanda', 'Goodbar', 'rgoodbar0@about.me', 'Non-binary', '1960-04-09', 'France');

ALTER TABLE person
DROP CONSTRAINT unique_email_address;