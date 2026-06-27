-- Write your query below

-- Write a query to find the names of all sellers who did not make 
-- any sales in the year 2020.
--Return the result ordered by seller_name in ascending order.

SELECT seller_name
FROM seller s
LEFT JOIN (
    SELECT order_id, seller_id
    FROM orders
    WHERE EXTRACT(YEAR FROM sale_date) = 2020
) AS o
ON s.seller_id = o.seller_id
WHERE o.seller_id IS NULL
ORDER BY seller_name;

