import re

class BankOperator:
    def __init__(self):
        self.users = []
        self.accounts = []
        self.transactions = []

    def create_user(self):
        email = input("Enter email: ")
        if not self.is_valid_email(email):
            print("Invalid email address!")
            return
        
        name = input("Enter name: ")
        self.users.append({"email": email, "name": name})
        print(f"User {name} created successfully.")

    def is_valid_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def list_users(self):
        if not self.users:
            print("No users available.")
            return
        
        for i, user in enumerate(self.users):
            print(f"{i + 1}. {user['name']} - {user['email']}")

    def create_account(self):
        if not self.users:
            print("No users available. Please create a user first.")
            return

        self.list_users()

        user_index = int(input("Select a user by number: ")) - 1
        if user_index < 0 or user_index >= len(self.users):
            print("Invalid user selection.\n")
            return

        account_type = input("Enter account type (Savings/Checking): ")
        if account_type not in ["Savings", "Checking"]:
            print("Invalid account type!")
            return

        user = self.users[user_index]
        account = {"user": user, "type": account_type, "balance": 0.0}
        self.accounts.append(account)
        print(f"{account_type} account created for {user['name']}.")

    def deposit_money(self):
        if not self.accounts:
            print("No accounts available to deposit into.")
            return
        
        self.list_accounts()

        account_index = int(input("Select account by number: ")) - 1
        if account_index < 0 or account_index >= len(self.accounts):
            print("Invalid account selection.\n")
            return
        
        amount = float(input("Enter deposit amount: "))
        self.accounts[account_index]["balance"] += amount
        self.transactions.append(f"Deposited ${amount} to {self.accounts[account_index]['user']['name']}'s account.")
        print(f"${amount} deposited successfully.")

    def withdraw_money(self):
        if not self.accounts:
            print("No accounts available to withdraw from.")
            return
        
        self.list_accounts()

        account_index = int(input("Select account by number: ")) - 1
        if account_index < 0 or account_index >= len(self.accounts):
            print("Invalid account selection.\n")
            return
        
        amount = float(input("Enter withdrawal amount: "))
        account = self.accounts[account_index]
        
        if account["balance"] < amount:
            print("Insufficient funds!")
            return
        
        account["balance"] -= amount
        self.transactions.append(f"Withdrew ${amount} from {account['user']['name']}'s account.")
        print(f"${amount} withdrawn successfully.")

    def list_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return
        
        for i, account in enumerate(self.accounts):
            print(f"{i + 1}. {account['user']['name']} - {account['type']} - Balance: ${account['balance']}")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return

        for transaction in self.transactions:
            print(transaction)
