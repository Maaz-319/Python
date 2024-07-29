import database_handler_user as db_user
import datetime

class User:
    def __init__(self, name, phone, email, address, account_type, balance, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = balance
        self.password = password
    
    def __str__(self):
        user_id = db_user.search(self.name)[0]
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        # get time in 12 hour format with AM/PM
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"ID: {user_id}\n{'-'*20}\nName: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\nBalance: {self.balance}\n{'-'*20}\nDate: {current_date}\nTime: {current_time}"

    def add_user(self):
        db_user.add_record(self)
        db_user.commit_changes()
    
    def update_user(self, new_name):
        db_user.update_record(self, new_name)
        db_user.commit_changes()
        self.name = new_name
    
    def delete_user(self):
        db_user.delete_record(self.name)
        db_user.commit_changes()
    
    def withdraw_money(self, amount):
        self.balance -= amount
        self.update_user(self.name)
        return self.balance
    
    def deposit_money(self, amount):
        self.balance += amount
        self.update_user(self.name)
        return self.balance
    
    def download_info(self):
        with open(f"INFO {self.name}.txt", "w") as file:
            file.write(str(self))
        return f"INFO {self.name}.txt"
