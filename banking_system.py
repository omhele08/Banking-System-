import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def check_balance(self):
        return f"Account {self.account_number} balance for {self.account_holder}: ${self.balance}"

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("400x400")

        # Set background color
        self.root.configure(bg='#F5F5F5')

        self.users = []  # List to store BankAccount objects
        self.current_user = None

        tk.Label(root, text="Account Holder Name:", bg='#F5F5F5').pack()
        self.account_holder_entry = tk.Entry(root, width=20)
        self.account_holder_entry.pack(pady=5)

        tk.Label(root, text="Account Number:", bg='#F5F5F5').pack()
        self.account_number_entry = tk.Entry(root, width=20)
        self.account_number_entry.pack(pady=5)

        tk.Button(root, text="Create User", command=self.create_user, bg='#4CAF50', fg='white', padx=10, pady=5, relief=tk.GROOVE).pack(pady=10)

        tk.Label(root, text="Amount:", bg='#F5F5F5').pack()
        self.amount_entry = tk.Entry(root, width=20)
        self.amount_entry.pack(pady=5)

        tk.Button(root, text="Deposit", command=self.deposit, bg='#008CBA', fg='white', padx=10, pady=5, relief=tk.GROOVE).pack(pady=5)
        tk.Button(root, text="Withdraw", command=self.withdraw, bg='#D9534F', fg='white', padx=10, pady=5, relief=tk.GROOVE).pack(pady=5)
        tk.Label(root, text="All Users:", bg='#F5F5F5').pack()
        self.user_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=5)
        self.user_listbox.pack(pady=5)

        tk.Button(root, text="Select User", command=self.select_user, bg='#5BC0DE', fg='white', padx=10, pady=5, relief=tk.GROOVE).pack(pady=5)

        self.balance_label = tk.Label(root, text="", bg='#F5F5F5', font=("Helvetica", 12))
        self.balance_label.pack(pady=10)

    def create_user(self):
        account_holder = self.account_holder_entry.get()
        account_number = self.account_number_entry.get()

        if account_holder and account_number:
            new_user = BankAccount(account_number, account_holder)
            self.users.append(new_user)
            self.update_user_list()
            messagebox.showinfo("User Created", f"User {account_holder} with Account Number {account_number} created successfully.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter Account Holder Name and Account Number.")

    def deposit(self):
        amount = self.get_amount()
        if amount is not None:
            result = self.current_user.deposit(amount)
            self.update_balance(result)

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None:
            result = self.current_user.withdraw(amount)
            self.update_balance(result)

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount < 0:
                messagebox.showwarning("Invalid Amount", "Please enter a positive amount.")
                return None
            return amount
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid numeric amount.")
            return None

    def select_user(self):
        selected_index = self.user_listbox.curselection()
        if selected_index:
            selected_user = self.users[selected_index[0]]
            self.current_user = selected_user
            self.balance_label.config(text=selected_user.check_balance())
        else:
            messagebox.showwarning("User Not Selected", "Please select a user from the list.")

    def update_user_list(self):
        self.user_listbox.delete(0, tk.END)
        for user in self.users:
            self.user_listbox.insert(tk.END, f"{user.account_number} - {user.account_holder}")

    def update_balance(self, message):
        self.balance_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()


