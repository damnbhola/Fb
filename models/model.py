from abc import ABCMeta, abstractmethod
from typing import Dict, List, TypeVar, Type
from common.database import Database

T = TypeVar("T", bound="Model")


class Model(metaclass=ABCMeta):
    collection: str
    _id: str

    def __init__(self, *args, **kwargs):
        pass

    def save_to_mongo(self):
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        elements_from_db = Database.find(cls.collection, {})
        if not elements_from_db:
            return []
        return [cls(**elem) for elem in elements_from_db]
