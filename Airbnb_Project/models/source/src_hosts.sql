WITH raw_hosts AS (
  SELECT * FROM AIRBNB.RAW.raw_hosts
)
SELECT
  id AS listing_id,
  name AS listing_name,
  is_superhost,
  created_at,
  updated_at
FROM
  raw_hosts
