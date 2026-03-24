# ✅ Features included:
# Add expense
# View all expenses
# Total calculation
# Data saved in file


import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "expenses.json"

# Load data
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        expenses = json.load(f)
else:
    expenses = []

# Save data
def save_data():
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f)

# Add expense
def add_expense():
    desc = entry_desc.get()
    amount = entry_amount.get()
    category = category_var.get()

    if desc == "" or amount == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    expense = {
        "desc": desc,
        "amount": float(amount),
        "category": category
    }

    expenses.append(expense)
    save_data()
    display_expenses()

    entry_desc.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# Display expenses
def display_expenses():
    listbox.delete(0, tk.END)
    total = 0

    for exp in expenses:
        listbox.insert(tk.END, f"{exp['desc']} - ₹{exp['amount']} ({exp['category']})")
        total += exp["amount"]

    label_total.config(text=f"Total: ₹{total}")

# Main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x500")

# Inputs
tk.Label(root, text="Description").pack()
entry_desc = tk.Entry(root)
entry_desc.pack()

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="Category").pack()
category_var = tk.StringVar(value="Food")
tk.OptionMenu(root, category_var, "Food", "Travel", "Shopping").pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack()

# Total label
label_total = tk.Label(root, text="Total: ₹0")
label_total.pack(pady=10)

display_expenses()

root.mainloop()