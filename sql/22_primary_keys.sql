SELECT
    *
FROM
    person
WHERE
    id = 1;

-- INSERT INTO
--     person (id, first_name, last_name, gender, email, date_of_birth, country_of_birth)
-- VALUES
--     (1, 'Alfreda', 'Beadon', 'Female', 'abeadon@example.com', '1953-10-28', 'Comoros');
-- ERROR:  duplicate key value violates unique constraint "person_pkey"
-- DETAIL:  Key (id)=(1) already exists.
ALTER TABLE person
DROP CONSTRAINT person_pkey;

INSERT INTO
    person (id, first_name, last_name, gender, email, date_of_birth, country_of_birth)
VALUES
    (1, 'Alfreda', 'Beadon', 'Female', 'abeadon@example.com', '1953-10-28', 'Comoros');

SELECT
    *
FROM
    person
WHERE
    id = 1;

DELETE FROM person
WHERE
    id = 1
    AND first_name = 'Alfreda';

ALTER TABLE person
ADD PRIMARY KEY (id);

SELECT
    *
FROM
    person
WHERE
    id = 1;