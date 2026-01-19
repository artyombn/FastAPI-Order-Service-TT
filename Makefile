include .env
export

DB_CONNECTION = postgresql://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@$(POSTGRES_HOST):$(POSTGRES_PORT)/$(POSTGRES_DB)

create_all_tables:
	psql $(DB_CONNECTION) -f database/schema.sql

filldb_categories:
	psql $(DB_CONNECTION) -f database/fill_db/categories.sql
