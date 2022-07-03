"""
How to Connect to mysql Docker from Python application on MacOS Mojave

https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa

"""

import sqlalchemy as db

# specify database configurations
config = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'pwd0123456789',
    'database': 'my_database'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')
# specify connection string
# psql postgresql://postgres:pwd0123456789@localhost:5432/my_database
connection_str = f'postgresql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = db.create_engine(connection_str)
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
# schema: information_schema
# Column: {'name': 'feature_id', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'feature_name', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'is_supported', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'is_verified_by', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'comments', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'feature_id', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'feature_name', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sub_feature_id', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sub_feature_name', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'is_supported', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'is_verified_by', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'comments', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'implementation_info_id', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'implementation_info_name', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'integer_value', 'type': INTEGER(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'character_value', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'comments', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'feature_id', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'feature_name', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'is_supported', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'is_verified_by', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'comments', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sql_language_source', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sql_language_year', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sql_language_conformance', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sql_language_integrity', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sql_language_implementation', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sql_language_binding_style', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sql_language_programming_language', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sizing_id', 'type': INTEGER(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sizing_name', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'supported_value', 'type': INTEGER(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'comments', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sizing_id', 'type': INTEGER(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'sizing_name', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'profile_id', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'required_value', 'type': INTEGER(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'comments', 'type': VARCHAR(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# schema: public
# Column: {'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'name', 'type': TEXT(), 'nullable': False, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'age', 'type': INTEGER(), 'nullable': False, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'address', 'type': CHAR(length=50), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'salary', 'type': REAL(), 'nullable': True, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'dept', 'type': CHAR(length=50), 'nullable': False, 'default': None, 'autoincrement': False, 'comment': None}
# Column: {'name': 'emp_id', 'type': INTEGER(), 'nullable': False, 'default': None, 'autoincrement': False, 'comment': None}