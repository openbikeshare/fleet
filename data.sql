CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE cycle_location (
    id                  VARCHAR(255),
    location            GEOGRAPHY,
    type                VARCHAR(255),
    system_id           VARCHAR(255),
    last_time_updated   TIMESTAMP,
    last_time_imported  TIMESTAMP,
    PRIMARY KEY(id)
);

CREATE TABLE station (
    id          VARCHAR(255),
    free_bikes  INTEGER,
    empty_slots INTEGER,
    max_bikes   INTEGER,
    open247     BOOLEAN
);

CREATE EXTENSION IF NOT EXISTS HSTORE;

CREATE TABLE cache (
  id serial PRIMARY KEY,
  name varchar,
  attributes hstore
);

INSERT INTO cache VALUES (1, 'geocache', hstore(ARRAY[['coverage', null]]));

