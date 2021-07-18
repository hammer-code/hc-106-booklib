from .base import Repository

class StudentRepository(Repository):
  def __init__(self, cnx):
    Repository.__init__(self, cnx)
    self.table_name = "students"
    self.columns = ("id", "user_id", "name", "number", "created_at", "updated_at")