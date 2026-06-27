-- Write your query below
SELECT name, SUM(
    CASE
        WHEN distance IS NULL THEN 0
        ELSE distance
    END
) AS travelled_distance
FROM users u
LEFT JOIN rides r
ON u.id = r.user_id
GROUP BY u.id
ORDER BY SUM(
    CASE
        WHEN distance IS NULL THEN 0
        ELSE distance
    END
) DESC, name;