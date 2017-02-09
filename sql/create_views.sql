DROP VIEW IF EXISTS products;
DROP VIEW IF EXISTS subcategories;
DROP VIEW IF EXISTS categories;
DROP VIEW IF EXISTS features;
DROP VIEW IF EXISTS binary_features;
DROP VIEW IF EXISTS feature_values;
DROP VIEW IF EXISTS feature_categories;

CREATE VIEW feature_categories AS
SELECT idgr AS id, gr00 AS name, gr01 as description
FROM pdegenskapsgrupper;

CREATE VIEW products AS
SELECT idpr AS id, pr09 AS name, pr11 as price, pr01 as description, pr18 as weight, pr20 as ean, pr21 as measurements
FROM pdprodukt
WHERE pr31 IS true;

CREATE VIEW subcategories AS
SELECT idka AS id, ka01 AS name, ka03 as description, ka02 AS category_id
FROM pdkategori;

CREATE VIEW categories AS
SELECT idhk AS id, hk00 AS name
FROM pdhuvudkategori;

CREATE VIEW binary_features AS
SELECT idet AS id, et04 AS name, et00 AS description, et03 AS value 
FROM pdegentyp where length(et03) - length(replace(et03, ',', '')) = 1;

CREATE VIEW features AS
SELECT idet AS id, et04 AS name, et00 AS description, et03 AS value, comparetype as compare_type
FROM pdegentyp
WHERE comparetype IN (1, 2, 3) AND et01 = 'Lista';

CREATE VIEW feature_values AS
SELECT eg00 as feature_id, eg02 as product_id, eg01 as value
FROM pdegenskap;