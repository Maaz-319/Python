from data import items_list
from database_handler import save_data_to_file


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save_item(self, order_data):
        items_list[self.name] = self.price
        save_data_to_file(items_list, order_data)

    def delete_item(self, order_data):
        items_list.pop(self.name)
        save_data_to_file(items_list, order_data)
