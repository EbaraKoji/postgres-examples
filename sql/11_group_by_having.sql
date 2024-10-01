SELECT
    country_of_birth,
    COUNT(*)
FROM
    person
GROUP BY
    country_of_birth
HAVING
    COUNT(*) >= 10
ORDER BY
    country_of_birth
LIMIT
    10;