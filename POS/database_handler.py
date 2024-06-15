def save_data_to_file(items_list, order_data):
    with open('data.py', 'w') as f:
        f.write(f'items_list = {items_list}\norder_data = {order_data}\n')
        f.close()
