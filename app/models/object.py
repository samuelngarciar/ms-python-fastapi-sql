from sqlalchemy import Column, Integer, String
from .base import Base

class SysObject(Base):
    __tablename__ = 'objects'
    __table_args__ = {'schema': 'sys'}
    
    object_id = Column(Integer, primary_key=True)
    name = Column(String)
    type_desc = Column(String)