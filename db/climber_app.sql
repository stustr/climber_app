DROP TABLE IF EXISTS hills;
DROP TABLE IF EXISTS climbers;
DROP TABLE IF EXISTS activities;
CREATE TABLE hills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    height INT,
    area = VARCHAR(255)
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
    self.climber = climber,
    self.hill = hill
);