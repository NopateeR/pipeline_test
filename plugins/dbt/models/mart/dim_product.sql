SELECT 
    ROW_NUMBER() OVER () AS product_id,
    product_name,
    product_expire
FROM (
    SELECT DISTINCT product_name,product_expire
    FROM {{ source('datalake.raw_data', 'sensor_data') }}
)