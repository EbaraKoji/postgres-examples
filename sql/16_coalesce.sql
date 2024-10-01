-- SELECT COALESCE(null, null, 1, 10) AS number; -- first non-null value
SELECT
    COALESCE(email, 'EMAIL NOT PROVIDED')
FROM
    person
LIMIT
    10;