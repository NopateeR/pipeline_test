# Datawow Data Platform

## Overview

This project is a dataplatform demo to ingest data generating from python code into PostgreSQL.

## Infrastructure
- Airflow
- PostgreSQL

## Pipeline Design
Split into three sections
1. Load data from parquet file into PostgreSQL using DuckDB
**Behind the design:**
- DuckDB is an analytical database management system. DuckDB has a built-in parquet reader and has PostgreSQL connector that could load the parquet file into PostgreSQL directly.


2. Transform data from PostgreSQL into data warehouse using DBT 
**Behind the design:**
- DBT is a data transformation tool with Cosmos' operator. DBT has postgres connector that could execute sql query and create table/view for us.  DBT provides framework to create and manage data warehouse.

## Table design
By applying the star schema design, data has been splitted into multiple dimensions and facts and generate the primary key and foreign key for the table.

- Dimension Table
    - dim_department
    - dim_product
    - dim_sensor
- Fact Table
    - fact_sensor

## local development
This environment is managed by **poetry** to help maintain python packages. 
This would maintain the same version of packages both on local machine and docker environment and also help local linting during development process.

Run the following command to install packages:
```bash
poetry install
```


-----
To Run a full loop pipeline
# 1. start up Airflow, PostgreSQL and Redis
```bash
docker-compose up -d --build
```

When then Airflow up and running , you could access Airflow via webserver.
Access Airflow webserver
http://localhost:8080
username : airflow
password : airflow
and also the postgresql that contain both the airflow database and datalake
Access postgresql
http://localhost:5432
username : airflow
password : airflow


# 2. Run pipeline 

- Select dag called 'src_data_generator' and trigger the pipeline
- DAG would generate data into parquet and then load into PostgreSQl and subsequently transform into star schema

