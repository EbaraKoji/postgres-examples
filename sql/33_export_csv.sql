\copy (SELECT * FROM person LEFT JOIN car ON car.id = person.car_id) TO sql/person_car.csv;