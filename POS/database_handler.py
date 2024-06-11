def save_data_to_file(items_name, items_price, order_data):
    with open('data.py', 'w') as f:
        f.write(f'items_name = {items_name}\nitems_price = {items_price}\norder_data = {order_data}\n')
        f.close()
