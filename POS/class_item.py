from data import items_name, items_price
from database_handler import save_data_to_file


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save_item(self, order_data):
        items_name.append(self.name)
        items_price.append(self.price)
        save_data_to_file(items_name, items_price, order_data)

    def delete_item(self, order_data):
        items_name.remove(self.name)
        items_price.remove(self.price)
        save_data_to_file(items_name, items_price, order_data)
