import database_handler_librarian as db_librarian


class Librarian:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def add_librarian(self):
        db_librarian.insert_data(self.name, self.password)
        db_librarian.commit_the_changes()
