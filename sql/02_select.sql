SELECT
    id,
    first_name,
    last_name,
    country_of_birth
FROM
    person
ORDER BY
    country_of_birth DESC,
    id ASC
LIMIT
    10;