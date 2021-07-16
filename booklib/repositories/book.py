from .base import Repository
from .book_author import BookAuthorRepository
from .author import AuthorRepository
class BookRepository(Repository):
  def __init__(self, cnx):
    Repository.__init__(self, cnx)
    self.table_name = "books"
    self.columns = (
      "id", "title", "published", "quantity",
      "image_url", "created_at", "updated_at",
    )

  def transform(self, columns, row):
    result = super().transform(columns, row)

    book_author_repo = BookAuthorRepository(self.cnx)
    book_authors = book_author_repo.filter({"book_id": row[0]})

    author_repo = AuthorRepository(self.cnx)
    authors = [
      author_repo.filter_by_id(book_author["author_id"])
      for book_author in book_authors
    ]
    result["authors"] = authors

    return result