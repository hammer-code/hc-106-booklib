from .base import Repository

class UserRepository(Repository):
  def __init__(self, cnx):
    Repository.__init__(self, cnx)
    self.table_name = "users"
    self.columns = ("id", "username", "password", "role", "created_at", "updated_at")