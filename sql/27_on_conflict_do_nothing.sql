-- "id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY" needs "OVERRIDING SYSTEM VALUE". When using old BIGSERIAL, it doesn't need.
-- INSERT INTO
--     person (id, first_name, last_name, email, gender, date_of_birth, country_of_birth) OVERRIDING SYSTEM VALUE
-- VALUES
--     (99999, 'Redford', 'Goodbar', 'rgoodbar0@about.me', NULL, '1960-04-09', 'France');
-- DELETE FROM person
-- WHERE
--     id = 99999;
INSERT INTO
    person (id, first_name, last_name, email, gender, date_of_birth, country_of_birth) OVERRIDING SYSTEM VALUE
VALUES
    (1, 'Redford', 'Goodbar', 'rgoodbar0@about.me', NULL, '1960-04-09', 'France') ON CONFLICT (id)
DO NOTHING;