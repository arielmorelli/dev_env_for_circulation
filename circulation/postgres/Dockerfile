FROM postgres:9.3

WORKDIR /

RUN echo "grant all privileges on database simplified_circ_db to simplified;" >> /docker-entrypoint-initdb.d/create_db.sql
RUN echo "create extension pgcrypto" >> /docker-entrypoint-initdb.d/create_db.sql

EXPOSE 5432

