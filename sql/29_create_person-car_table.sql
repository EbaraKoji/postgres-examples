DROP TABLE IF EXISTS person;

DROP TABLE IF EXISTS car;

CREATE TABLE
    car (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        make VARCHAR(50) NOT NULL,
        model VARCHAR(50) NOT NULL,
        price NUMERIC(19, 2) NOT NULL
    );

CREATE TABLE
    person (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(50),
        gender VARCHAR(50),
        date_of_birth DATE NOT NULL,
        country_of_birth VARCHAR(50),
        car_id INT REFERENCES car (id), -- adding `ON DELETE CASCADE` raises no error in 32_delete_with_foreign_keys.sql
        UNIQUE (car_id)
    );

INSERT INTO
    car (make, model, price)
VALUES
    ('Buick', 'Coachbuilder', '16352.22');

INSERT INTO
    car (make, model, price)
VALUES
    ('Volkswagen', 'New Beetle', '34002.30');

INSERT INTO
    car (make, model, price)
VALUES
    ('Nissan', 'Pathfinder', '37358.62');

INSERT INTO
    car (make, model, price)
VALUES
    ('Dodge', 'Ram 1500', '26632.26');

INSERT INTO
    car (make, model, price)
VALUES
    ('Suzuki', 'SJ', '68965.93');

INSERT INTO
    person (first_name, last_name, email, gender, date_of_birth, country_of_birth, car_id)
VALUES
    ('Redford', 'Goodbar', 'rgoodbar0@about.me', NULL, '1960-04-09', 'France', 1);

INSERT INTO
    person (first_name, last_name, email, gender, date_of_birth, country_of_birth, car_id)
VALUES
    ('Cherida', 'Weight', 'cweight1@addthis.com', 'Female', '2011-09-27', 'Russia', 2);

INSERT INTO
    person (first_name, last_name, email, gender, date_of_birth, country_of_birth, car_id)
VALUES
    ('Currey', 'Pregel', 'cpregel2@dion.ne.jp', 'Male', '2013-05-10', 'Peru', 4);

INSERT INTO
    person (first_name, last_name, email, gender, date_of_birth, country_of_birth)
VALUES
    ('Dominga', 'Zmitrovich', 'dzmitrovich3@chron.com', 'Female', '1992-01-08', 'Indonesia');

INSERT INTO
    person (first_name, last_name, email, gender, date_of_birth, country_of_birth)
VALUES
    ('Rance', 'Emmanueli', 'remmanueli4@angelfire.com', 'Male', '1978-04-05', 'Japan');