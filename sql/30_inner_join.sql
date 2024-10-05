SELECT
    person.id, first_name, car_id, make, model, price
FROM
    person
    JOIN car ON person.car_id = car.id;