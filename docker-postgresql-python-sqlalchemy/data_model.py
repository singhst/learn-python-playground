'''
Declare a Class in Python to map to db tables
https://docs.sqlalchemy.org/en/14/orm/tutorial.html
'''

#########################################
# 1 Declare Data Models
#########################################
import datetime
from typing import List
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, nullable=False, primary_key=True)
    company_code = Column(String(256), nullable=False, index=True)
    name = Column(String(256), nullable=False)
    ceo = Column(String(256), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return f"User(id={self.id!r}, company_code={self.company_code!r}, name={self.name!r}, ceo={self.ceo!r})"
