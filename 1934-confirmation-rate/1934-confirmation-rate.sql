WITH partA AS (
    SELECT s.user_id,
           COUNT(*) AS con
    FROM Signups s
    JOIN Confirmations c
      ON s.user_id = c.user_id
    WHERE c.action = 'confirmed'
    GROUP BY s.user_id
),
partC AS (
    SELECT s.user_id,
           COUNT(*) AS total   
    FROM Signups s
    left JOIN Confirmations c
      ON s.user_id = c.user_id
    GROUP BY s.user_id
)

SELECT c.user_id,
       round((IFNULL(a.con, 0) / c.total),2) AS confirmation_rate
FROM partC c
LEFT JOIN partA a
  ON c.user_id = a.user_id;
