CREATE DATABASE your_database_name;

\c your_database_name;

CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  address VARCHAR(200),
  city VARCHAR(100),
  state VARCHAR(100),
  country VARCHAR(100),
  location geometry(Point, 4326)
);

