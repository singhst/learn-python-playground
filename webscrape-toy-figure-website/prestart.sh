#! /usr/bin/env bash

# Let the DB start
# = Try to create session to check if DB is awake
python ./app/backend_pre_start.py

# Create DB migration file (i.e. = a `.py` to act as SQL DDL to create/alter tables' columns/data types etc.)
alembic revision --autogenerate -m "Added initial table"

# Run migrations
alembic upgrade head        #<--- ALEMBIC MIGRATION COMMAND

# Create initial data in DB
python ./app/initial_data.py