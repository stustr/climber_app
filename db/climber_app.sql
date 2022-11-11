DROP TABLE IF EXISTS hills CASCADE;
DROP TABLE IF EXISTS climbers CASCADE;
DROP TABLE IF EXISTS ascents;
CREATE TABLE hills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    height FLOAT,
    area VARCHAR(255)
);
CREATE TABLE climbers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
CREATE TABLE ascents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    time FLOAT,
    description VARCHAR,
    climber_id SERIAL NOT NULL REFERENCES climbers(id),
    hill_id SERIAL NOT NULL REFERENCES hills(id)
);