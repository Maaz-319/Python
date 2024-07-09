import database_handler_order as db_order


class Order:
    def __init__(self, customer_id, items, date_time, cashier, total_price, quantity):
        self.customer_id = customer_id
        self.items = list(items)
        self.date_time = date_time
        self.cashier = cashier
        self.total_price = total_price
        self.quantity = list(quantity)

    def save_order(self, order_text):
        order_text = f"Order No. {self.customer_id}\nCashier: {self.cashier}\nTime: {self.date_time}\n{'-' * 20}\nItem Name - Price - Quantity\n{'-' * 20}\n{order_text}\n\n{'-' * 20}\nTotal Price: Rs {self.total_price}\n"

        for item, quantity in zip(self.items, self.quantity):
            db_order.insert_data(self.customer_id, item.name, self.date_time, self.cashier, self.total_price,
                                 quantity)

        db_order.commit_the_changes()
        return order_text
