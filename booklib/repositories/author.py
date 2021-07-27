from .base import Repository

class AuthorRepository(Repository):
  def __init__(self):
    Repository.__init__(self)
    self.table_name = "authors"
    self.columns = ("id", "name", "created_at", "updated_at")