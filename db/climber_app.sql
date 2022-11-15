DROP TABLE IF EXISTS hills CASCADE;
DROP TABLE IF EXISTS climbers CASCADE;
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS ascents;
CREATE TABLE hills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    height FLOAT,
    area VARCHAR(255),
    image_path VARCHAR(500),
    route_link VARCHAR(255), 
    weather_path VARCHAR(500)
);
CREATE TABLE climbers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
CREATE TABLE ratings (
    id SERIAL PRIMARY KEY,
    hill SERIAL NOT NULL REFERENCES hills(id),
    score INT 
);
CREATE TABLE ascents (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    description VARCHAR,
    climber_id SERIAL NOT NULL REFERENCES climbers(id),
    hill_id SERIAL NOT NULL REFERENCES hills(id)
);