DROP TABLE shoes;
DROP TABLE brands;

CREATE TABLE brands (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE shoes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255), 
  category VARCHAR(255), 
  buying_cost VARCHAR(255), 
  selling_cost VARCHAR(255), 
  number_of_shoes VARCHAR(255), 
  brand_id INT REFERENCES brands(id) ON DELETE CASCADE
);
