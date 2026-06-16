FROM apache/airflow:3.2.2-python3.12

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/airflow/.local/bin:$PATH"

USER airflow

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY --chown=airflow:root pyproject.toml poetry.lock /opt/airflow/

WORKDIR /opt/airflow
RUN poetry install --no-root --no-interaction --no-ansi --verbose

RUN python -c "import duckdb; con = duckdb.connect(); con.execute('INSTALL postgres;')"


EXPOSE 8080 5555 6379