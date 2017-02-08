CREATE VIEW products_with_features AS
SELECT id,
       name,
       array_to_json(array(SELECT v.value
                           FROM features
                           LEFT JOIN (SELECT *
                                      FROM feature_values
                                      WHERE feature_values.product_id = products.id) AS v 
                           ON features.id = v.feature_id
                           ORDER BY features.id))
FROM products
ORDER BY products.id;

\copy (SELECT * FROM products_with_features) TO '../data/products.csv' DELIMITER ',' CSV

DROP VIEW products_with_features;