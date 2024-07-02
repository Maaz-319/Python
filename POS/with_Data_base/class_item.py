import database_handler_item as db_item


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save_item(self):
        db_item.insert_data(self.name, self.price)
        db.commit_the_changes()

    def delete_item(self):
        db_item.delete_item(self.name)
        db_item.commit_the_changes()

    def update_item(self):
        db_item.modify_item_price(self.name, self.price)
        db_item.commit_the_changes()
