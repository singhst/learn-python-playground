"""
How to Connect to mysql Docker from Python application on MacOS Mojave

https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa

"""

from sqlalchemy import text, create_engine
import configparser

full_config_file_path = "./config.ini"
config = configparser.ConfigParser()
config.read(full_config_file_path)

SQLALCHEMY_DATABASE_URI = config["sqlite"].get("connection_str") #"sqlite:///example.db"    #database connection string
print(SQLALCHEMY_DATABASE_URI)

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

### (1.1) create table
sql = text("""
CREATE TABLE IF NOT EXISTS company (
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    company_code varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    ceo varchar(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
db.execute(sql)
print(">>> 1.1 raw sql created table")

sql = text("""
DROP TABLE IF EXISTS company;
""")
db.execute(sql)
print(">>> 1.1 raw sql dropped table")

### (1.2) create table
# https://docs.sqlalchemy.org/en/14/orm/tutorial.html
from sqlalchemy import MetaData
from data_model import Base
Base.metadata.create_all(engine)
print(">>> 1.2 Python Class created table")


### (2) insert data
data = ({"id": 1, "company_code":"N1", "name": "The Hobbit",         "ceo": "Tolkien",},
        {"id": 2, "company_code":"D2", "name": "The Silmarillion",   "ceo": "Tolkien"},
        {"id": 3, "company_code":"G1", "name": "Google",             "ceo": "aaa"},
        {"id": 4, "company_code":"I4", "name": "NVDA",               "ceo": "bbb"},
        )

for line in data:
    sql = text("""
    INSERT INTO company(id, company_code, name, ceo) VALUES(:id, :company_code, :name, :ceo)
    """)
    _engine = db.get_bind()
    _engine.execute(sql, **line)

### (2) sql bulk insert
sql = text("""
INSERT INTO company(id, company_code, name, ceo) VALUES 
(99,'c99','bulk1','ceo1'),
(88,'p88','bulk2','ceo2'),
(77,'e77','bulk3','ceo3'),
(66,'h66','bulk4','ceo4');
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
#     (1, 'N1', 'The Hobbit', 'Tolkien'),
#     (2, 'D2', 'The Silmarillion', 'Tolkien'),
#     (3, 'G1', 'Google', 'aaa'),
#     (4, 'I4', 'NVDA', 'bbb'),
#     (99, 'c99', 'bulk1', 'ceo1'),
#     (88, 'p88', 'bulk2', 'ceo2'),
#     (77, 'e77', 'bulk3', 'ceo3'),
#     (66, 'h66', 'bulk4', 'ceo4')
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
# Column: {'name': 'id', 'type': INTEGER(), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 1}
# Column: {'name': 'company_code', 'type': VARCHAR(length=255), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'name', 'type': VARCHAR(length=255), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
# Column: {'name': 'ceo', 'type': VARCHAR(length=255), 'nullable': False, 'default': None, 'autoincrement': 'auto', 'primary_key': 0}
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