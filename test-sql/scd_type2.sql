SELECT t1.cus_id, t1.*
FROM older_snapshot_table t1
INNER JOIN (
  SELECT cus_id, MAX(dbt_updated_at) AS max_dbt_updated_at
  FROM older_snapshot_table
  GROUP BY cus_id
) t2 
  ON t1.cus_id = t2.cus_id 
  AND t1.dbt_updated_at = t2.max_dbt_updated_at

UNION

SELECT t3.cus_id, t3.*
FROM newer_snapshot_table t3
INNER JOIN (
  SELECT cus_id, MAX(dbt_updated_at) AS max_dbt_updated_at
  FROM newer_snapshot_table
  GROUP BY cus_id
) t4 
  ON t3.cus_id = t4.cus_id 
  AND t3.dbt_updated_at = t4.max_dbt_updated_at;