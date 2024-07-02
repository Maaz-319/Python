from data import cashier_login, current_cashier


def save_data_to_file(items_list, order_data):
    with open('data.py', 'w') as f:
        f.write(
            f'items_list = {items_list}\norder_data = {order_data}\ncashier_login = {cashier_login}\ncurrent_cashier = "{current_cashier}"\n')
        f.close()
