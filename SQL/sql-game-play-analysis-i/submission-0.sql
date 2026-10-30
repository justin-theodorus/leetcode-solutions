-- Write your query below
WITH rankings AS (
    SELECT player_id, event_date,
        RANK() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS ranking
    FROM activity
)
SELECT player_id, event_date AS first_login
FROM rankings
WHERE ranking = 1;
