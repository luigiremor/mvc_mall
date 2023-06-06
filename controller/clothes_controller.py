import tkinter as tk
from model.clothes_model import ClothesModel
from view.clothes_view import ClothesView
from view.login_view import LoginView


class ClothesAppController:
    def __init__(self):
        self.build()
        self.model = ClothesModel()
        self.login_view = LoginView(self.root, self)
        self.root.mainloop()

    def build(self):
        self.root = tk.Tk()

    def authenticate_user(self, username, password):
        # Replace with your authentication logic
        if username == "admin" and password == "password":
            return True
        else:
            return False

    def login_successful(self):
        self.login_view.root.destroy()  # Close the login window
        self.build()
        self.view = ClothesView(self.root, self.model)
        self.root.title("Clothes Mall")
        self.root.geometry("600x400")
        self.root.mainloop()
