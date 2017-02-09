CREATE VIEW cellphone_attributes AS
SELECT attributes.id, attributes.name, attributes.value, attributes.compare_type
FROM attributes
JOIN attribute_subcategories
ON attributes.id = attribute_subcategories.attribute_id
JOIN subcategories
ON attribute_subcategories.subcategory_id = subcategories.id
WHERE subcategories.name = 'Mobiltelefon';

CREATE VIEW cellphones_with_attributes AS
SELECT products.id,
       products.name,
       array_to_json(array(SELECT v.value
                           FROM cellphone_attributes
                           LEFT JOIN (SELECT *
                                      FROM attribute_values
                                      WHERE attribute_values.product_id = products.id) AS v 
                           ON cellphone_attributes.id = v.attribute_id
                           ORDER BY cellphone_attributes.id))
FROM products
JOIN subcategories
ON products.subcategory_id = subcategories.id
WHERE subcategories.name = 'Mobiltelefon'
ORDER BY products.id;

\copy (SELECT name, value, compare_type FROM cellphone_attributes) TO '../data/cellphone_attributes.csv' DELIMITER ',' CSV
\copy (SELECT * FROM cellphones_with_attributes) TO '../data/cellphones.csv' DELIMITER ',' CSV

DROP VIEW cellphones_with_attributes;
DROP VIEW cellphone_attributes;