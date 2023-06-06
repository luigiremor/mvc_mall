import sqlite3


class ClothesModel:
    def __init__(self):
        self.conn = sqlite3.connect("clothes.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        self.observers = []

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS clothes (id INTEGER PRIMARY KEY, name TEXT, price REAL)")

    def add_clothes(self, name, price):
        self.cursor.execute(
            "INSERT INTO clothes (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()
        self.notify_observers()

    def get_all_clothes(self):
        self.cursor.execute("SELECT * FROM clothes")
        return self.cursor.fetchall()

    def update_clothes(self, id, name, price):
        self.cursor.execute(
            "UPDATE clothes SET name=?, price=? WHERE id=?", (name, price, id))
        self.conn.commit()
        self.notify_observers()

    def delete_clothes(self, id):
        self.cursor.execute("DELETE FROM clothes WHERE id=?", (id,))
        self.conn.commit()
        self.notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()
