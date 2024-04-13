import sqlite3

class connect():
    def __init__(self):
        self.connection = sqlite3.connect('Database/data.db')
        self.cur = self.connection.cursor()

    def update_transact_data(self, data):
        ar_value = data['ar']
        name_value = data['name']
        id_value = data['id']
        self.connection = sqlite3.connect('Database/data.db')
        self.cur = self.connection.cursor()
        self.cur.execute("SELECT name FROM userdata WHERE  id = ?", [id_value])
        data = self.cur.fetchall()
        if len(data) == 0:
            print("New Account Added")
            self.cur.execute("INSERT INTO userdata (id, name, ar) VALUES (?, ?, ?)",
                             (id_value, name_value, ar_value))
            self.connection.commit()
            return
        self.cur.execute("UPDATE userdata SET ar = ar + ? WHERE id = ?", (ar_value, id_value))
        # self.cur.execute("INSERT INTO userdata (id, name, ar) VALUES (?, ?, ?)",
        #                  (id_value, name_value, ar_value))
        self.connection.commit()
    def update_new_account(self, data):
        name_value = data['name']
        id_value = data['id']
        id = id_value
        self.connection = sqlite3.connect('Database/data.db')
        self.cur = self.connection.cursor()
        self.cur.execute("SELECT name FROM userdata WHERE  id = ?", [id_value])
        data = self.cur.fetchall()
        if len(data) > 0:
            return False
        self.cur.execute("INSERT INTO userdata (id, name, ar) VALUES (?, ?, ?)",
                         (id, name_value, 0))
        print(id)
        self.connection.commit()
        return True

    def __del__(self):
        self.connection.commit()
        self.connection.close()
