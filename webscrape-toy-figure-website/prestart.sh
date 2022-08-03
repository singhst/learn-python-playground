#! /usr/bin/env bash

# Let the DB start
# = Try to create session to check if DB is awake
python ./app/backend_pre_start.py

# Run migrations
alembic upgrade head        #<--- ALEMBIC MIGRATION COMMAND

# Create initial data in DB
python ./app/initial_data.py