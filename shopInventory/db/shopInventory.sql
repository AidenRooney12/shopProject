DROP TABLE brands;
DROP TABLE shoes;

CREATE TABLE shoes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE brands (
 id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  shoe_id INT REFERENCES shoes(id) ON DELETE CASCADE
);
