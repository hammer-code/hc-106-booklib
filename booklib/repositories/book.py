from .base import Repository
from .book_author import BookAuthorRepository
from .author import AuthorRepository


class BookRepository(Repository):
    def __init__(self):
        Repository.__init__(self)
        self.table_name = "books"
        self.columns = (
            "id",
            "title",
            "published",
            "quantity",
            "image_url",
            "created_at",
            "updated_at",
        )

    def transform(self, columns, row):
        result = super().transform(columns, row)
        book_author_repo = BookAuthorRepository()
        book_authors = book_author_repo.filter_by({"book_id": result["id"]})
        author_repo = AuthorRepository()
        authors = list(
            map(
                lambda book_author: author_repo.filter_by_id(book_author["author_id"]),
                book_authors,
            )
        )
        result["authors"] = authors
        return result

    def create(self, data):
        authors = data["authors"]
        del data["authors"]
        book = super().create(data)
        book_author_repo = BookAuthorRepository()
        for author_id in authors:
            if author_id != "":
                data = {"book_id": book["id"], "author_id": author_id}
                book_author_repo.create(data)

        return book

    def update(self, book_id, data):
        authors = []
        if "authors" in data:
            authors = data["authors"]
            del data["authors"]
        book = super().update(book_id, data)
        book_author_repo = BookAuthorRepository()
        book_authors = book_author_repo.filter_by({"book_id": book_id})
        for book_author in book_authors:
            book_author_repo.delete(book_author["id"])
        if authors:
            for author_id in authors:
                if author_id != "":
                    data = {"book_id": book["id"], "author_id": author_id}
                    book_author_repo.create(data)

        return book

    def delete(self, book_id):
        book_author_repo = BookAuthorRepository()
        book_authors = book_author_repo.filter_by({"book_id": book_id})
        for book_author in book_authors:
            book_author_repo.delete(book_author["id"])
        super().delete(book_id)
