SELECT
    id,
    first_name,
    gender,
    country_of_birth,
    date_of_birth
FROM
    person
WHERE
    gender = 'Female'
    AND (
        country_of_birth = 'Poland'
        OR country_of_birth = 'Ukraine'
    )
ORDER BY
    date_of_birth DESC
LIMIT
    10;