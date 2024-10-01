SELECT DISTINCT
    gender
FROM
    person;

ALTER TABLE person
ADD CONSTRAINT gender_constraint CHECK (
    gender = 'Female'
    OR gender = 'Male'
);

INSERT INTO
    person (first_name, last_name, email, gender, date_of_birth, country_of_birth)
VALUES
    ('Fernanda', 'Goodbar', 'rgoodbar0@about.me', 'Non-binary', '1960-04-09', 'France');

ALTER TABLE person
DROP CONSTRAINT gender_constraint;