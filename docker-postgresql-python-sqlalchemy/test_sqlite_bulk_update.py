"""
Steps for using ORM,
https://docs.sqlalchemy.org/en/14/orm/quickstart.html
"""

# #########################################
# # 1 Declare Data Models
# #########################################
from typing import List
from sqlalchemy import Column, Integer, String, null
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, nullable=False, primary_key=True)
    company_code = Column(String(256), nullable=False)
    name = Column(String(256), nullable=False)
    ceo = Column(String(256), nullable=False)

    def __repr__(self):
        return f"User(id={self.id!r}, company_code={self.company_code!r}, name={self.name!r}, ceo={self.ceo!r})"



#########################################
# 2 Create an Engine
#########################################
from sqlalchemy import text, create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"    #database connection string

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
_data = [
    {"company_code":"c99", "name":"bulk1",             "ceo":"bulk update"},
    {"company_code":"e77", "name":"bulk update e77",   "ceo":"ceo3"},
    {"company_code":"po7", "name":"bulk insert po7",   "ceo":"jake"},
    {"company_code":"qwe", "name":"bulk insert qwe",   "ceo":"Karen"},
    ]

# Split `update` and `insert` data

### (1) Get all data in the DB
_original_companies = db.query(Company).all()
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
        _new_company["id"] = null
        _insert.append(_new_company)

print(">>> _update={}".format(_update))
print(">>> _insert={}".format(_insert))


# Bulk update
db.bulk_update_mappings(Company, _update)
db.commit()

results = db.query(Company).all()
print(results)

# # Bulk insert
# db.bulk_insert_mappings(Company, _insert)
# db.commit()

# results = db.query(Company).all()
# print(results)