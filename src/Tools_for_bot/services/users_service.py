from typing import Dict, Optional, List

from src.Tools_for_bot.models.user import User


class UsersService:
    def __init__(self):
        self.users: Dict[int, User] = {}
    
    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)
    
    def create_user(self, user_id: int) -> User:
        user = User(id=user_id)
        self.users[user_id] = user
        return user
    
    def get_or_create_user(self, user_id: int) -> User:
        user = self.get_user(user_id)
        if user is None:
            user = self.create_user(user_id)
        return user
    
    def update_user(self, user: User) -> User:
        self.users[user.id] = user
        return user
    
    def get_all_users(self) -> List[User]:
        return list(self.users.values())
    
users_service = UsersService()