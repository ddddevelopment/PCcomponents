from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    name: str
    age: int
    email: str
    username: Optional[str] = None
    
    def is_registered(self) -> bool:
        return bool(self.name and self.age and self.email)
    
    def __str__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', age={self.age}, email='{self.email}')"
    