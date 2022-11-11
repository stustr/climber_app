DROP TABLE IF EXISTS hills;
DROP TABLE IF EXISTS climbers;
DROP TABLE IF EXISTS activities;
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
CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    time FLOAT,
    description VARCHAR,
    climber_id SERIAL NOT NULL REFERENCES climbers(id) ON DELETE CASCADE,
    hill_id SERIAL NOT NULL REFERENCES hills(id) ON DELETE CASCADE
);