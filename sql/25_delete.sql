INSERT INTO
    person (first_name, last_name, email, gender, date_of_birth, country_of_birth)
VALUES
    ('Fernanda', 'Goodbar', 'rgoodbar0@about.me', 'Non-binary', '1960-04-09', 'France');

DELETE FROM person
WHERE
    first_name = 'Fernanda'
    AND email = 'rgoodbar0@about.me';