from .base import Repository


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
