import database_handler_transaction as db_transaction

class Transaction:
    def __init__(self, transaction_id, transaction_type, transaction_amount, transaction_date, transaction_time):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_date = transaction_date
        self.transaction_time = transaction_time

    def __str__(self):
        return f"Type: {self.transaction_type}\nAmount: {self.transaction_amount}\nDate: {self.transaction_date}\nTime: {self.transaction_time}"

    def save_transaction(self):
        db_transaction.add_record(self)
        db_transaction.commit_changes()
