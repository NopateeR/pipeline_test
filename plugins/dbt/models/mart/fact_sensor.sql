SELECT
    ROW_NUMBER() OVER () AS fact_key,
    d.department_id,
    s.sensor_id,
    p.product_id,
    src.create_at
FROM {{ source('datalake.raw_data', 'sensor_data') }} src
JOIN {{ ref('dim_department') }} d
    ON src.department_name = d.department_name
JOIN {{ ref('dim_sensor') }} s
    ON src.sensor_serial = s.sensor_serial
JOIN {{ ref('dim_product') }} p
    ON src.product_name = p.product_name
   AND src.product_expire = p.product_expire