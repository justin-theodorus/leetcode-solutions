WITH volumes AS (
    SELECT product_id, SUM(width * length * height) AS volume
    FROM products
    GROUP BY product_id
)
SELECT w.name AS warehouse_name, SUM(v.volume * w.units) AS volume
FROM warehouse w
JOIN volumes v ON w.product_id = v.product_id
GROUP BY w.name;

