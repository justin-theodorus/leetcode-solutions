-- Write your query below
WITH rankings AS (
    SELECT user_id, time_stamp,
        RANK() OVER (PARTITION BY user_id ORDER BY time_stamp DESC) AS ranking
    FROM logins
    WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
)

SELECT user_id, time_stamp AS last_stamp
FROM rankings
WHERE ranking = 1;


