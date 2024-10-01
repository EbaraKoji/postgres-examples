SELECT
    MAX(price)
FROM
    car;

SELECT
    MIN(price)
FROM
    car;

SELECT
    ROUND(AVG(price), 2)
FROM
    car;

SELECT
    make,
    model,
    MIN(price),
    MAX(price)
FROM
    car
GROUP BY
    make,
    model
LIMIT
    5;