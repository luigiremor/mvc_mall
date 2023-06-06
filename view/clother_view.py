from tkinter import messagebox
import tkinter as tk


class ClothesView:
    def __init__(self, root, model):
        self.root = root
        self.root.title("Clothes Mall CRUD App")
        self.model = model

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        self.price_label = tk.Label(self.root, text="Price:")
        self.price_label.grid(row=1, column=0)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=1, column=1)

        self.add_button = tk.Button(
            self.root, text="Add", command=self.add_clothes)
        self.add_button.grid(row=2, column=0)

        self.clothes_listbox = tk.Listbox(self.root)
        self.clothes_listbox.grid(row=3, columnspan=5)
        self.clothes_listbox.bind("<<ListboxSelect>>", self.select_clothes)

        self.update_button = tk.Button(
            self.root, text="Update", command=self.update_clothes)
        self.update_button.grid(row=4, column=0)

        self.delete_button = tk.Button(
            self.root, text="Delete", command=self.delete_clothes)
        self.delete_button.grid(row=4, column=1)

        self.model.add_observer(self)

    def display_clothes(self, clothes):
        self.clothes_listbox.delete(0, tk.END)
        for cloth in clothes:
            self.clothes_listbox.insert(
                tk.END, f"{cloth[0]}. {cloth[1]} - ${cloth[2]}")

    def add_clothes(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        if name and price:
            self.model.add_clothes(name, price)
            self.name_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Input Error", "Please enter a name and price.")

    def select_clothes(self, event):
        selected_index = self.clothes_listbox.curselection()
        if selected_index:
            selected_clothes = self.clothes_listbox.get(selected_index)
            self.selected_id = int(selected_clothes.split(".")[0])

    def update_clothes(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        if name and price and hasattr(self, "selected_id"):
            self.model.update_clothes(self.selected_id, name, price)
            self.name_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            del self.selected_id
        else:
            messagebox.showwarning(
                "Selection Error", "Please select an item and provide a name and price.")

    def delete_clothes(self):
        if hasattr(self, "selected_id"):
            self.model.delete_clothes(self.selected_id)
            self.name_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            del self.selected_id
        else:
            messagebox.showwarning("Selection Error", "Please select an item.")

    def update(self):
        self.display_clothes(self.model.get_all_clothes())
