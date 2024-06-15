from data import items_list
from database_handler import save_data_to_file


class Order:
    def __init__(self, customer_id, items):
        self.customer_id = customer_id
        self.items = list(items)

    def save_order(self, order_text, total_price, order_data):
        order_text = f"Order No. {self.customer_id}\n{order_text}\n\nTotal Price: Rs {total_price}"
        order_data.append(order_text)
        save_data_to_file(items_list, order_data)
        return order_text
