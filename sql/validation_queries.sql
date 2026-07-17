-- DuckDB validation queries
SELECT COUNT(*) AS row_count FROM cleaned;
SELECT COUNT(*) - (SELECT COUNT(*) FROM (SELECT DISTINCT * FROM cleaned)) AS duplicate_rows FROM cleaned;
SELECT COUNT(*) AS invalid_duration FROM cleaned WHERE trip_duration_minutes <= 0;
SELECT COUNT(*) AS invalid_zone FROM cleaned WHERE pulocationid NOT BETWEEN 1 AND 265 OR dolocationid NOT BETWEEN 1 AND 265;
SELECT COUNT(*) AS hard_invalid FROM cleaned WHERE is_hard_invalid;
SELECT COUNT(*) AS suspicious FROM cleaned WHERE is_suspicious;
