DROP TABLE older_snapshot_table;
CREATE TABLE iF NOT EXISTS older_snapshot_table (
  row_id VARCHAR(10),
  cus_id VARCHAR(10),
  dbt_updated_at DATE,
  valid_start_from DATE,
  valid_end_at DATE
);
-- Insert the data into the table
INSERT INTO older_snapshot_table (row_id, cus_id, dbt_updated_at, valid_start_from, valid_end_at)
VALUES
  ('r1', 'cus_1', '2023-09-01', '2023-09-01', '2023-10-01'),
  ('r2', 'cus_1', '2023-10-01', '2023-10-01', NULL),
  ('r3', 'cus_2', '2023-10-01', '2023-10-01', NULL),
  ('r4', 'cus_3', '2023-10-01', '2023-10-01', NULL);

--
DROP TABLE newer_snapshot_table;
CREATE TABLE iF NOT EXISTS newer_snapshot_table (
  row_id VARCHAR(10),
  cus_id VARCHAR(10),
  dbt_updated_at DATE,
  valid_start_from DATE,
  valid_end_at DATE
);

-- Insert the data into the table
INSERT INTO newer_snapshot_table (row_id, cus_id, dbt_updated_at, valid_start_from, valid_end_at)
VALUES
  ('r1', 'cus_1', '2023-09-01', '2023-09-01', '2023-10-01'),
  ('r2', 'cus_1', '2023-10-01', '2023-10-01', '2023-10-24'),
  ('r3', 'cus_2', '2023-10-01', '2023-10-01', '2023-10-24'),
  ('r4', 'cus_3', '2023-10-01', '2023-10-01', NULL),
  ('r6', 'cus_2', '2023-10-24', '2023-10-24', NULL),
  ('r7', 'cus_1', '2023-10-24', '2023-10-24', NULL);