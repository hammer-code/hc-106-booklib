from .base import Repository


class UserRepository(Repository):
    def __init__(self):
        Repository.__init__(self)
        self.table_name = "users"
        self.columns = (
            "id",
            "username",
            "password",
            "role",
            "created_at",
            "updated_at",
        )
