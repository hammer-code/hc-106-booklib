from .base import Repository
from .book import BookRepository
from .student import StudentRepository


class BorrowedRepository(Repository):
    def __init__(self):
        Repository.__init__(self)
        self.table_name = "borroweds"
        self.columns = (
            "id",
            "receipt_number",
            "book_id",
            "student_id",
            "returned",
            "created_at",
            "updated_at",
        )

    def transform(self, columns, row):
        result = super().transform(columns, row)
        book_repo = BookRepository()
        book = book_repo.filter_by_id(result["book_id"])
        student_repo = StudentRepository()
        student = student_repo.filter_by_id(result["student_id"])
        result["book"] = book
        result["student"] = student
        return result
