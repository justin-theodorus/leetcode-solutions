-- Write your query below

-- Write a query to find the names of all sellers who did not make 
-- any sales in the year 2020.
--Return the result ordered by seller_name in ascending order.

SELECT seller_name
FROM seller s
WHERE s.seller_id NOT IN (
    SELECT seller_id
    FROM orders
    WHERE EXTRACT(YEAR FROM sale_date) = 2020
)
ORDER BY seller_name;

