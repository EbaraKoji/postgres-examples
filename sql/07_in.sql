SELECT
    id,
    first_name,
    country_of_birth
FROM
    person
    -- WHERE country_of_birth = 'China'
    -- OR country_of_birth = 'France'
    -- OR country_of_birth = 'Brazil'
WHERE
    country_of_birth IN ('China', 'France', 'Brazil')
LIMIT
    15;