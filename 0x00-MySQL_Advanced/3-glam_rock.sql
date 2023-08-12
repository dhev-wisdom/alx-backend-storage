--  SQL script that lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT band_name,
IFNULL(TIMESTAMPDIFF(YEAR, formed, split), TIMESTAMPDIFF(YEAR, formed, 2022)) AS lifespan
FROM metal_bands
WHERE style LIKE %Glam Rock%
ORDER BY lifespan DESC;
