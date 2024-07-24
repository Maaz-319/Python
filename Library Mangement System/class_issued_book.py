import database_handler_issued_book as db_issued_book
import database_handler_user as db_user


class IssuedBook:
    def __init__(self, book_name, user_id, issue_date, membership, return_date):
        self.book_name = book_name
        self.user_id = user_id
        self.issue_date = issue_date
        self.membership = membership
        self.return_date = return_date

    def __str__(self):
        user_name = db_user.get_user_by_id(self.user_id)
        return f"Book: {self.book_name}\nUser: {user_name}\nIssue Date: {self.issue_date}\nReturn Date: {self.return_date}"

    def save_new_issued_book(self):
        db_issued_book.add_record(self.book_name, self.user_id, self.issue_date, self.membership, self.return_date)
        db_issued_book.commit_changes()

    @staticmethod
    def show_all_issued_books():
        return db_issued_book.show_all()

    def delete_issued_book(self):
        db_issued_book.delete_record(self.book_name)
        db_issued_book.commit_changes()

    def search_issued_book(self, mode=0):  # mode 0 means book name, 1 means user id
        return db_issued_book.search(self.book_name, mode)
