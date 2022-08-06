from typing import Generic, List, Type, TypeVar
from app.db.base_class import Base
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)

class databseHelper():
    def bulkInsert(self,
                   db: Session,
                   db_table_data_model: Type[ModelType],
                   data_in: List[dict]):
        db.bulk_insert_mappings(db_table_data_model, data_in)
        db.commit()

    def bulkUpdate(self,
                   db: Session,
                   db_table_data_model: Type[ModelType],
                   data_in: List[dict]):
        db.bulk_update_mappings(db_table_data_model, data_in)
        db.commit()
