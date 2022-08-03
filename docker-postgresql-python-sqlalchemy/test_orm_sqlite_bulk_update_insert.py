"""
Steps for using ORM,
https://docs.sqlalchemy.org/en/14/orm/quickstart.html
"""

# #########################################
# # 1 Declare Data Models
# #########################################
from data_model import Company


#########################################
# 2 Create an Engine
#########################################
import configparser
config = configparser.ConfigParser()
config.read("./config.ini")
SQLALCHEMY_DATABASE_URI = config["sqlite"].get("connection_str") #"sqlite:///example.db"    #database connection string
print(SQLALCHEMY_DATABASE_URI)


from sqlalchemy import text, create_engine
from sqlalchemy.orm import sessionmaker

# [For SQLite connection]
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # echo=False, # stop printing SQL statement when doing CRUD operations
    echo=True,
    # only required for sqlite
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()



# #########################################
# # 3 Emit CREATE TABLE DDL
# #########################################
# Base.metadata.create_all(engine)



#########################################
# 4 Query table
#########################################
sql = text("""
SELECT * 
from company 
""")
results = db.execute(sql)
print(list(results))



#########################################
# 5 Bulk update
#########################################
from typing import List

_data = [
    {"company_code":"c99", "name":"bulk1",             "ceo":"bulk update"},
    {"company_code":"e77", "name":"bulk update e77",   "ceo":"ceo3"},
    {"company_code":"po7", "name":"bulk insert po7",   "ceo":"jake"},
    {"company_code":"qwe", "name":"bulk insert qwe",   "ceo":"Karen"},
    ]

# Split `update` and `insert` data

### (1) Get all data in the DB
_original_companies = db.query(Company).all()
_max_id = max([_.id for _ in _original_companies])
_original_company_codes = [company.company_code for company in _original_companies]

### (2) split
_update: List = []
_insert: List = []
for _new_company in _data:
    _new_company_code = _new_company.get("company_code")
    if _new_company_code in _original_company_codes:
        _original_company_id = [_company.id for _company in _original_companies if _company.company_code == _new_company_code][0]
        _new_company["id"] = _original_company_id
        _update.append(_new_company)
    else:
        _max_id += 1
        _new_company["id"] = _max_id
        _insert.append(_new_company)

print(">>> _update={}".format(_update))
print(">>> _insert={}".format(_insert))


### (3.1) Bulk update
db.bulk_update_mappings(Company, _update)
db.commit()

results = db.query(Company).all()
print(results)

### (3.2) Bulk insert
db.bulk_insert_mappings(Company, _insert)
db.commit()

results = db.query(Company).all()
print(results)