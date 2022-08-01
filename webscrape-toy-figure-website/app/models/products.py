from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Products(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=True)
    shop_product_code = Column(String(256), nullable=True)
    order_time_start = Column(DateTime, nullable=True)
    order_time_end = Column(DateTime, nullable=True)
    delivery_date = Column(DateTime, nullable=True)
    company = Column(String(256), nullable=True)
    original_website = Column(String(256), nullable=True)
    img_url = Column(String(256), nullable=True)
    order_status = Column(String(256), nullable=True)
    is_favourite = Column(Boolean, default=False)
    create_at = Column(DateTime, nullable=True)
    create_by = Column(String(256), nullable=True)
    update_at = Column(DateTime, nullable=True)
    update_by = Column(String(256), nullable=True)
