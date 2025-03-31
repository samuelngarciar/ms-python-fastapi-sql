from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.object import SysObject
import logging

class ObjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_objects(self, limit: int, offset: int):
        try:
            results = self.db.query(SysObject.object_id, SysObject.name, SysObject.type_desc).order_by(SysObject.object_id).limit(limit).offset(offset).all()
            return [{"object_id": obj.object_id, "name": obj.name, "type_desc": obj.type_desc} for obj in results]
        except SQLAlchemyError as e:
            logging.error(f"Error fetching objects: {e}")
            return {"error": "An error occurred while fetching objects."}