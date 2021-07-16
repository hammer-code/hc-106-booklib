from .base import Repository

class BookAuthorRepository(Repository):
  def __init__(self, cnx):
    self.cnx = cnx
    self.table_name = "book_authors"
    self.columns = (
      "id", "book_id", "author_id", "created_at", "updated_at",
    )