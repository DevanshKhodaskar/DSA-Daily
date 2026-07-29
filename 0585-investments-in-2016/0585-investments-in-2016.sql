WITH cordCount AS (
    SELECT
        lat,
        lon,
        COUNT(*) AS cnt
    FROM Insurance
    GROUP BY lat, lon
),
repeated AS (
    SELECT
        tiv_2015,
        COUNT(*) AS cnt
    FROM Insurance
    GROUP BY tiv_2015
)



SELECT Round(sum(tbl.tiv_2016),2) as tiv_2016
FROM (
    SELECT i1.*
    FROM Insurance i1
    JOIN cordCount c
      ON i1.lat = c.lat
     AND i1.lon = c.lon
    WHERE c.cnt = 1
) tbl
JOIN repeated r
  ON tbl.tiv_2015 = r.tiv_2015
WHERE r.cnt > 1;