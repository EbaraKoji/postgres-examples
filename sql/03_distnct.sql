SELECT DISTINCT
    country_of_birth
FROM
    person
ORDER BY
    country_of_birth
LIMIT
    10;

SELECT
    COUNT(DISTINCT country_of_birth)
FROM
    person;