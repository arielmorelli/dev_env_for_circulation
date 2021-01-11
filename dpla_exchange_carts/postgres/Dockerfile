FROM postgres:9.3

WORKDIR /

COPY postgres/create_tables.sql /docker-entrypoint-initdb.d/create_db.sql

EXPOSE 5432

