include .env
export

DB_CONNECTION = postgresql://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@$(POSTGRES_HOST):$(POSTGRES_PORT)/$(POSTGRES_DB)

create_all_tables:
	psql $(DB_CONNECTION) -f database/schema.sql

filldb:
	make filldb_categories && \
	make filldb_clients

filldb_categories:
	psql $(DB_CONNECTION) -f database/fill_db/categories.sql

filldb_clients:
	psql $(DB_CONNECTION) -f database/fill_db/clients.sql
