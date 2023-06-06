from tkinter import messagebox
import tkinter as tk


class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Login")
        self.controller = controller

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(
            self.root, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.authenticate_user(username, password):
            self.controller.login_successful()
        else:
            messagebox.showerror(
                "Login Failed", "Invalid username or password.")
