import tkinter as tk
from tkinter import messagebox

# Dictionary to store account details
accounts = {}

# ---------------- FUNCTIONS ---------------- #

def create_account():
    acc_no = entry_acc.get()
    name = entry_name.get()
    balance = entry_balance.get()

    if acc_no == "" or name == "" or balance == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    if acc_no in accounts:
        messagebox.showerror("Error", "Account already exists!")
        return

    try:
        balance = float(balance)
        if balance < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid balance!")
        return

    accounts[acc_no] = {
        "name": name,
        "balance": balance,
        "transactions": []
    }

    messagebox.showinfo("Success", "Account Created Successfully!")
    clear_fields()


def deposit():
    acc_no = entry_acc.get()
    amount = entry_amount.get()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid deposit amount!")
        return

    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["transactions"].append(f"Deposited ₹{amount}")

    messagebox.showinfo("Success", "Amount Deposited Successfully!")
    clear_fields()


def withdraw():
    acc_no = entry_acc.get()
    amount = entry_amount.get()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid withdrawal amount!")
        return

    if accounts[acc_no]["balance"] < amount:
        messagebox.showerror("Error", "Insufficient Balance!")
        return

    accounts[acc_no]["balance"] -= amount
    accounts[acc_no]["transactions"].append(f"Withdrawn ₹{amount}")

    messagebox.showinfo("Success", "Amount Withdrawn Successfully!")
    clear_fields()


def check_balance():
    acc_no = entry_acc.get()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    name = accounts[acc_no]["name"]
    balance = accounts[acc_no]["balance"]

    messagebox.showinfo("Account Details",
                        f"Account Holder: {name}\nCurrent Balance: ₹{balance:.2f}")


def delete_account():
    acc_no = entry_acc.get()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    del accounts[acc_no]
    messagebox.showinfo("Success", "Account Deleted Successfully!")
    clear_fields()


def show_transactions():
    acc_no = entry_acc.get()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    transactions = accounts[acc_no]["transactions"]

    if not transactions:
        messagebox.showinfo("Transactions", "No transactions yet.")
    else:
        messagebox.showinfo("Transactions", "\n".join(transactions))


def clear_fields():
    entry_acc.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_balance.delete(0, tk.END)
    entry_amount.delete(0, tk.END)


# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Banking Management System")
root.geometry("400x500")
root.config(bg="lightblue")
root.resizable(False, False)

tk.Label(root, text="Banking Management System",
         font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

tk.Label(root, text="Account Number", bg="lightblue").pack()
entry_acc = tk.Entry(root)
entry_acc.pack()

tk.Label(root, text="Name", bg="lightblue").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Initial Balance", bg="lightblue").pack()
entry_balance = tk.Entry(root)
entry_balance.pack()

tk.Label(root, text="Amount", bg="lightblue").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Button(root, text="Create Account", command=create_account,
          bg="green", fg="white").pack(pady=5)

tk.Button(root, text="Deposit", command=deposit,
          bg="blue", fg="white").pack(pady=5)

tk.Button(root, text="Withdraw", command=withdraw,
          bg="red", fg="white").pack(pady=5)

tk.Button(root, text="Check Balance", command=check_balance,
          bg="purple", fg="white").pack(pady=5)

tk.Button(root, text="Delete Account", command=delete_account,
          bg="black", fg="white").pack(pady=5)

tk.Button(root, text="Transaction History",
          command=show_transactions,
          bg="orange", fg="white").pack(pady=5)

root.mainloop()
