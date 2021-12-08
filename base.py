import sqlite3

class DBController:
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def get_user(self, user_id):
        self.cursor.execute(
            "SELECT * FROM users WHERE id = '{}';".format(user_id)
        )
        obj = self.cursor.fetchone()
        if obj:
            return True

    def valut(self, user_id):
        self.cursor.execute(
            "SELECT * FROM users WHERE id = '{};'".format(user_id)
        )

    def add_account(self, user_id, ans_curs):
        self.cursor.execute(
            f"INSERT INTO users (id, curs) VALUES ( '{user_id}', '{ans_curs}' );")
        self.connection.commit()

    def get_saved(self, user_id):
        self.cursor.execute(
            f"SELECT * FROM users where id = {user_id}"
        )

        one_result = self.cursor.fetchone()[1]
        return one_result

    def delete_user(self, user_id):
        self.cursor.execute(
            f"DELETE FROM users WHERE id = {user_id}"
        )
        self.connection.commit()