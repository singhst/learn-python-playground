"""
How to Connect to mysql Docker from Python application on MacOS Mojave

https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa

"""

import sqlalchemy as db

# # specify database configurations
# config = {
#     'host': 'localhost',
#     'port': 5432,
#     'user': 'postgres',
#     'password': 'pwd0123456789',
#     'database': 'my_database'
# }
# db_user = config.get('user')
# db_pwd = config.get('password')
# db_host = config.get('host')
# db_port = config.get('port')
# db_name = config.get('database')
# # specify connection string
# # psql postgresql://postgres:pwd0123456789@localhost:5432/my_database
# connection_str = f'postgresql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# # connect to database
# engine = db.create_engine(connection_str)

SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"    #database connection string

# [For SQLite connection]
engine = db.create_engine(
    SQLALCHEMY_DATABASE_URI,
    # only required for sqlite
    connect_args={"check_same_thread": False},
)

connection = engine.connect()
# pull metadata of a table
print(connection)
### output
# <sqlalchemy.engine.base.Connection object at 0x103f16e80>

metadata = db.MetaData(bind=engine)
metadata.reflect(only=['company'])

test_table = metadata.tables['company']

print(test_table)
### output 
# company

################################################

# Print schema of all tables in database

from sqlalchemy import inspect
inspector = inspect(engine)
schemas = inspector.get_schema_names()

for schema in schemas:
    print("schema: %s" % schema)
    for table_name in inspector.get_table_names(schema=schema):
        for column in inspector.get_columns(table_name, schema=schema):
            print("Column: %s" % column)

### Output
# schema: main
# Column: {'name': 'version_num', 'type': VARCHAR(length=32), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 1}
# Column: {'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'name', 'type': TEXT(length=25), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 1}
# Column: {'name': 'label', 'type': VARCHAR(length=256), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'url', 'type': VARCHAR(length=256), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'source', 'type': VARCHAR(length=256), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'submitter_id', 'type': INTEGER(), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 1}
# Column: {'name': 'first_name', 'type': VARCHAR(length=256), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'surname', 'type': VARCHAR(length=256), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'email', 'type': VARCHAR(), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'is_superuser', 'type': BOOLEAN(), 'nullable': True, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}