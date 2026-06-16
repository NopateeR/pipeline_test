SELECT 
    ROW_NUMBER() OVER () AS department_id,
    department_name
FROM (
    SELECT DISTINCT department_name
    FROM {{ source('datalake.raw_data', 'sensor_data') }}
)