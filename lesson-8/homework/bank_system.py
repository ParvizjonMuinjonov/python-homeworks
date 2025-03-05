class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit must be non-negative.")
            return None
        account_number = len(self.accounts) + 1
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()  # Persist the new account
        print(f"Account created with number {account_number}.")
        return account_number
    
    def view_account(self):
        try:
            account_number = int(input("Input account number: "))
            if account_number in self.accounts:
                account = self.accounts[account_number]
                print(f"Account Number: {account.account_number}")
                print(f"Name: {account.name}")
                print(f"Balance: {account.balance}")
            else:
                print(f"Account number {account_number} not found.")
        except ValueError:
            print("Please enter a valid account number.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= 0:
                print("Deposit amount must be positive.")
                return
            account = self.accounts[account_number]
            account.balance += amount
            self.save_to_file()  # Persist the updated balance
            print(f"Deposited {amount} to account number {account_number}. New balance: {account.balance}")
        else:
            print(f"Account number {account_number} not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                return
            if account.balance >= amount:
                account.balance -= amount
                self.save_to_file()  # Persist the updated balance
                print(f"Withdrew {amount} from account number {account_number}. New balance: {account.balance}")
            else:
                print(f"Insufficient balance in account number {account_number}.")
        else:
            print(f"Account number {account_number} not found.")

    def save_to_file(self):
        try:
            with open("accounts.txt", "w") as file:
                for account_number, account in self.accounts.items():
                    file.write(f"{account_number},{account.name},{account.balance}\n")
        except IOError:
            print("Error saving to file.")

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                for line in file:
                    account_number, name, balance = line.strip().split(",")
                    account = Account(int(account_number), name, float(balance))
                    self.accounts[int(account_number)] = account
        except FileNotFoundError:
            print("No existing accounts file found. Starting fresh.")
        except (IOError, ValueError):
            print("Error loading file or invalid data format. Starting with empty accounts.")


# Main program to test the Bank class
def main():
    bank = Bank()
    bank.load_from_file()  # Load existing accounts at startup
    
    while True:
        print("\n=== Bank Menu ===")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter account holder name: ")
            try:
                initial_deposit = float(input("Enter initial deposit: "))
                bank.create_account(name, initial_deposit)
            except ValueError:
                print("Please enter a valid deposit amount.")
                
        elif choice == "2":
            bank.view_account()
            
        elif choice == "3":
            try:
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                bank.deposit(account_number, amount)
            except ValueError:
                print("Please enter valid numeric values.")
                
        elif choice == "4":
            try:
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(account_number, amount)
            except ValueError:
                print("Please enter valid numeric values.")
                
        elif choice == "5":
            print("Thank you for using the bank system. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()