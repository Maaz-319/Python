import database_handler_cashier as db_cashier


class Cashier:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def add_cashier(self):
        db_cashier.insert_data(self.name, self.password)
        db_cashier.commit_the_changes()
