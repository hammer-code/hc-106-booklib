from .base import Repository

class AuthorRepository(Repository):
  def __init__(self, cnx):
    Repository.__init__(self, cnx)
    self.table_name = "authors"
    self.columns = ("id", "name", "created_at", "updated_at")