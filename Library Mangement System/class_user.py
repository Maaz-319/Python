import database_handler_user as db_user


class User:
    def __init__(self, i_d, name, phone, email, membership):
        self.i_d = i_d
        self.name = name
        self.phone = phone
        self.email = email
        self.membership = membership

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nMembership: {self.membership}"

    def save_new_user(self):
        db_user.add_record(self.i_d, self.name, self.phone, self.email, self.membership)
        db_user.commit_changes()

    @staticmethod
    def show_all_users():
        return db_user.show_all()

    def update_user(self):
        db_user.update_record(self.name, self.email, self.phone)
        db_user.commit_changes()

    def delete_user(self, mode=0):  # mode 0 means user name
        db_user.delete_record(self.name, mode)
        db_user.commit_changes()

    def search_user(self, mode=0):  # mode 0 means user name
        return db_user.search(self.name, mode)
