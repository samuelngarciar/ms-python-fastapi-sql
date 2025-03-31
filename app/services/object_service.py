from app.repositories.object_repository import ObjectRepository

class ObjectService:
    def __init__(self, object_repository: ObjectRepository):
        self.object_repository = object_repository

    def get_objects(self, limit: int, offset: int):
        return self.object_repository.get_objects(limit, offset)
