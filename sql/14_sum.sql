SELECT
    make,
    SUM(price)
FROM
    car
GROUP BY
    make
LIMIT
    10;