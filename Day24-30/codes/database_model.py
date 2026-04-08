from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,String,Integer,Float

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "shop_products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)