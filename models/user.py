import uuid
from typing import Dict
from dataclasses import dataclass, field
from models.model import Model
from datetime import date


@dataclass(eq=False)
class User(Model):
    collection: str = field(init=False, default="users")
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password,
        }
