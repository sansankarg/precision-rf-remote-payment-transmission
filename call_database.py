import sqlite3

class connect():
    def __init__(self):
        self.connection = sqlite3.connect('Database/data.db')
        self.cur = self.connection.cursor()

    def update_transact_data(self, data):
        sender = data['sender']
        reciever = data['reciever']
        ar = data['ar']
        self.connection = sqlite3.connect('Database/data.db')
        self.cur = self.connection.cursor()
        self.cur.execute("SELECT fname FROM userbank_details WHERE  sid = ?", [sender])
        data1 = self.cur.fetchall()
        self.cur.execute("SELECT fname FROM userbank_details WHERE  rid = ?", [reciever])
        data2 = self.cur.fetchall()
        if len(data) == 0:
            # print("New Account Added")
            # self.cur.execute("INSERT INTO userdata (id, name, ar) VALUES (?, ?, ?)",
            #                  (id_value, name_value, ar_value))
            # self.connection.commit()
            return
        self.cur.execute("INSERT INTO transactions_data (sid, rid, ar) VALUES (?, ?, ?)",
                         (sender, reciever, ar))
        self.cur.execute("UPDATE userbank_details SET ar = ar + ? WHERE rid = ?", (ar, reciever))
        self.cur.execute("UPDATE userbank_details SET ar = ar - ? WHERE sid = ?", (ar, sender))
        # self.cur.execute("INSERT INTO userdata (id, name, ar) VALUES (?, ?, ?)",
        #                  (id_value, name_value, ar_value))
        self.connection.commit()
        print("Executed succesfullly")
    def update_new_account(self, data):
        fname_value = data['fname']
        lname_value = data['lname']
        sid_value = data['sid']
        rid_value = data['rid']
        age_value = data['age']
        self.connection = sqlite3.connect('Database/data.db')
        self.cur = self.connection.cursor()
        self.cur.execute("SELECT fname FROM userbank_details WHERE  rid = ?", [rid_value])
        data = self.cur.fetchall()
        if len(data) > 0:
            return False
        self.cur.execute("INSERT INTO userbank_details (sid, rid, fname, lname, age, ar) VALUES (?, ?, ?, ?, ?, ?)",
                         (sid_value, rid_value, fname_value, lname_value, age_value, 0))
        print(id)
        self.connection.commit()
        return True

    def __del__(self):
        self.connection.commit()
        self.connection.close()
