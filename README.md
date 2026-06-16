# Datawow Data Platform

## Overview

This project is a dataplatform demo to ingest data generating from python code into PostgreSQL.

## Infrastructure
- Airflow
- PostgreSQL
- 
## Pipeline Design
Split into three sections
1. Load data from parquet file into PostgreSQL
2. Transform data from PostgreSQL into data warehouse

## local development
This environment is managed by **poetry** to help maintain python packages. 
This would maintain the same version of packages both on local machine and docker environment and also help local linting during development process.

Run the following command to install packages:
```bash
poetry install
```


## Usage
- docker-compose up -d
