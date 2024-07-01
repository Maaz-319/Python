from data import items_list, current_cashier
from database_handler import save_data_to_file


class Order:
    def __init__(self, customer_id, items):
        self.customer_id = customer_id
        self.items = list(items)

    def save_order(self, order_text, total_price, order_data, date_time):
        order_text = f"Order No. {self.customer_id}\nCashier: {current_cashier}\nTime: {date_time}\n{'-'*20}\nItem Name - Price - Quantity\n{'-'*20}\n{order_text}\n\n{'-'*20}\nTotal Price: Rs {total_price}\n"
        order_data.append(order_text)
        save_data_to_file(items_list, order_data)
        return order_text
