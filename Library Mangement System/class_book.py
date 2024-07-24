import database_handler_book as db_book


class Book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Title: {self.name}\nAuthor: {self.author}\nGenre: {self.genre}"

    def save_new_book(self):
        go = db_book.add_record(self.name, self.author, self.genre)
        db_book.commit_changes()
        return go

    @staticmethod
    def show_all_books():
        return db_book.show_all()

    def update_book(self):
        db_book.update_record(self.name, self.author, self.genre)
        db_book.commit_changes()

    def delete_book(self):
        db_book.delete_record(self.name)
        db_book.commit_changes()

    def search_book(self, mode=0):  # mode 0 means book name, 1 author, 2 genre
        return db_book.search_book_by_mode(self.name, mode)