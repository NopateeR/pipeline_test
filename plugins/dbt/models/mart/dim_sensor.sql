

SELECT 
    ROW_NUMBER() OVER () AS sensor_id,
    sensor_serial
FROM (
    SELECT DISTINCT sensor_serial
    FROM {{ source('datalake.raw_data', 'sensor_data') }}
)