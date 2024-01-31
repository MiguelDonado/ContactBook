import sqlite3
import re
from tabulate import tabulate


class ContactBook:
    def __init__(self, name_table):
        self.name_database = "ContactBook.sqlite"
        self.name_table = name_table + "_Contacts"
        self.create()

    @property
    def name_table(self):
        return self._name_table

    @name_table.setter
    def name_table(self, name_table):
        self._name_table = name_table

    def execute_sql(
        self, sql, parameter_sql=None, read=False
    ):  # It's used by the CRUD methods, to reduce boilerplate code regarding the sqlite3 module"
        miConexion = sqlite3.connect(self.name_database)
        miCursor = miConexion.cursor()
        if parameter_sql == None:  # not parameterezid query (create,read)
            miCursor.execute(sql)
            if read:
                if contacts := miCursor.fetchall():
                    print(
                        tabulate(
                            contacts,
                            headers=(
                                "ID",
                                "Name",
                                "Address",
                                "Phone",
                                "Email",
                                "Change_At",
                            ),
                            tablefmt="pretty",
                        )
                    )
                else:
                    print("The ContactBook is empty.")
        else:  # parameterezid query (insert,delete,update,search)
            miCursor.execute(sql, parameter_sql)
            if read:
                if contact := miCursor.fetchone():  # if contact found
                    print(
                        tabulate(
                            ((contact),),
                            headers=(
                                "ID",
                                "Name",
                                "Address",
                                "Phone",
                                "Email",
                                "Change_At",
                            ),
                            tablefmt="pretty",
                        )
                    )
                else:
                    print("Contact not found.")
        miConexion.commit()
        miConexion.close()

    def check_exists(
        self, phone
    ):  # It's call by the methods DELETE and UPDATE to check if the phone indicated exists"
        miConexion = sqlite3.connect(self.name_database)
        miCursor = miConexion.cursor()
        miCursor.execute(
            f"SELECT name FROM {self.name_table} WHERE PHONE = ?", (phone,)
        )
        if contact := miCursor.fetchone():
            return True
        else:
            return False

    def create(self):
        sql = (
            f"CREATE TABLE IF NOT EXISTS {self.name_table} (ID INTEGER PRIMARY KEY AUTOINCREMENT,"
            f"NAME VARCHAR(50),ADDRESS VARCHAR(50),PHONE VARCHAR(15) UNIQUE,EMAIL VARCHAR(50),"
            f"CHANGE_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        )
        self.execute_sql(sql)

    def insert(self, name, address, phone, email):
        data = (name, address, phone, email)
        sql = (
            f"INSERT INTO {self.name_table} (NAME,ADDRESS,PHONE,EMAIL) VALUES (?,?,?,?)"
        )
        self.execute_sql(sql, data)

    def delete(self, phone):
        if self.check_exists(phone):
            sql = f"DELETE FROM {self.name_table} WHERE PHONE=?"
            self.execute_sql(sql, (phone,))
            print("Contact deleted")
        else:
            print("Contact not found")

    def read(self, order=None):
        if not order:
            sql = f"SELECT * FROM {self.name_table}"
            self.execute_sql(sql, read=True)
        else:
            sql = f"SELECT * FROM {self.name_table} " + f"ORDER BY {order}"
            self.execute_sql(sql, read=True)

    def update(self, prev_phone, name, address, phone, email):
        if self.check_exists(prev_phone):
            data = (name, address, phone, email, prev_phone)
            sql = f"UPDATE {self.name_table} SET NAME = ?, ADDRESS = ?, PHONE = ?, EMAIL = ?, CHANGE_AT = CURRENT_TIMESTAMP  WHERE PHONE=?"
            self.execute_sql(sql, data)
            print("Contact updated")
        else:
            print("Contact not found")

    def search(self, phone):
        sql = f"SELECT * FROM {self.name_table} WHERE PHONE=?"
        self.execute_sql(sql, (phone,), True)
