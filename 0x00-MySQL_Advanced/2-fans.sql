-- SQL script that ranks country origins of bands
-- ordered by the number of (non-unique) fans
source metal_bands.sql.zip
SELECT origin, SUM(nb_fans) AS total_fans
FROM bands
GROUP BY origin
ORDER BY total_fans DESC;
