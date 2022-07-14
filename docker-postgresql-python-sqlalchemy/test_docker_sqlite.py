"""
How to Connect to mysql Docker from Python application on MacOS Mojave

https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa

"""

from sqlalchemy import text, create_engine

SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"    #database connection string

# [For SQLite connection]
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # only required for sqlite
    connect_args={"check_same_thread": False},
)

connection = engine.connect()
# pull metadata of a table
print(connection)
### output
# <sqlalchemy.engine.base.Connection object at 0x103f16e80>


#########################################

from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print(SessionLocal)
### output
# sessionmaker(class_='Session', bind=Engine(sqlite:///example.db), autoflush=False, autocommit=False, expire_on_commit=True)


#########################################
# Implement raw sql
# 
#########################################

db = SessionLocal()

# write the SQL query inside the text() block

### (0) drop table
sql = text("""
DROP TABLE IF EXISTS company;
""")
db.execute(sql)

### (1) create table
sql = text("""
CREATE TABLE IF NOT EXISTS company (
	id int NOT NULL,
	name varchar(255) NOT NULL,
	ceo varchar(255) NOT NULL
);
""")
db.execute(sql)

### (2) insert data
data = ({"id": 1, "name": "The Hobbit", "ceo": "Tolkien"},
        {"id": 2, "name": "The Silmarillion", "ceo": "Tolkien"},
        {"id": 3, "name": "Google", "ceo": "aaa"},
        {"id": 4, "name": "NVDA", "ceo": "bbb"},
        )

for line in data:
    sql = text("""
    INSERT INTO company(id, name, ceo) VALUES(:id, :name, :ceo)
    """)
    _engine = db.get_bind()
    _engine.execute(sql, **line)

### (2) sql bulk insert
sql = text("""
INSERT INTO company(id, name, ceo) VALUES 
(99,'bulk1','ceo1'),
(88,'bulk2','ceo2'),
(77,'bulk3','ceo3'),
(66,'bulk4','ceo4');
""")
# db.execute(sql)       #not work
_engine = db.get_bind()
_engine.execute(sql)


### (3) query table
sql = text("""
SELECT * 
from company 
""")

results = db.execute(sql)
print(list(results))

### Output
# [
#     (1, 'The Hobbit', 'Tolkien'),
#     (2, 'The Silmarillion', 'Tolkien'),
#     (3, 'Google', 'aaa'),
#     (4, 'NVDA', 'bbb')
# ]

################################################

from sqlalchemy import MetaData

metadata = MetaData(bind=engine)
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