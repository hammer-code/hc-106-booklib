from .base import Repository

class BookRepository(Repository):
  def __init__(self, cnx):
    Repository.__init__(self, cnx)
    self.table_name = "books"
    self.columns = (
      "id", "title", "published", "quantity",
      "image_url", "created_at", "updated_at",
    )