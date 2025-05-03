class Account:
    def __init__(self, acc_no, name, age, address):
        if age < 18:
            raise ValueError("Account holder must be at least 18 years old.")
        self.acc_no = acc_no
        self.name = name
        self.age = age
        self.address = address
        self.balance = 0.0
        self.statement = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount
        self.statement.append(f"Deposited ₹{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.statement.append(f"Withdrew ₹{amount:.2f}")

    def update_info(self, name=None, age=None, address=None):
        if age is not None and age < 18:
            raise ValueError("Account holder must be at least 18 years old.")
        if name:
            self.name = name
        if age:
            self.age = age
        if address:
            self.address = address
        self.statement.append("Account information updated.")

    def show_balance(self):
        return self.balance

    def print_statement(self):
        print("\nTransaction Statement:")
        for entry in self.statement:
            print(" -", entry)
        print(f"Current Balance: ₹{self.balance:.2f}\n")

    def show_details(self):
        print("\nAccount Details:")
        print(f"Account Number: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Balance: ₹{self.balance:.2f}\n")


class Bank:
    def __init__(self):
        self.accounts = {}
        self.account_sequence = 1001

    def create_account(self, name, age, address):
        acc_no = self.account_sequence
        account = Account(acc_no, name, age, address)
        self.accounts[acc_no] = account
        self.account_sequence += 1
        return acc_no

    def get_account(self, acc_no):
        if acc_no not in self.accounts:
            raise KeyError("Account number not found.")
        return self.accounts[acc_no]

    def run(self):
        while True:
            print("\n--- Bank Menu ---")
            print("1. Create Account")
            print("2. Update Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Show Balance")
            print("6. Show Statement")
            print("7. Show Account Details")
            print("8. Exit")

            try:
                choice = int(input("Enter your choice (1-8): "))

                if choice == 1:
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    address = input("Enter address: ")
                    acc_no = self.create_account(name, age, address)
                    print(f"Account created successfully!\nAccount No: {acc_no}")

                elif choice == 2:
                    acc_no = int(input("Enter account number: "))
                    account = self.get_account(acc_no)
                    name = input("Enter new name (or press Enter to skip): ")
                    age_input = input("Enter new age (or press Enter to skip): ")
                    address = input("Enter new address (or press Enter to skip): ")
                    age = int(age_input) if age_input else None
                    account.update_info(name or None, age, address or None)
                    print("Account updated successfully.")

                elif choice == 3:
                    acc_no = int(input("Enter account number: "))
                    account = self.get_account(acc_no)
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print("Amount deposited successfully.")

                elif choice == 4:
                    acc_no = int(input("Enter account number: "))
                    account = self.get_account(acc_no)
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                    print("Amount withdrawn successfully.")

                elif choice == 5:
                    acc_no = int(input("Enter account number: "))
                    account = self.get_account(acc_no)
                    print(f"Current Balance: ₹{account.show_balance():.2f}")

                elif choice == 6:
                    acc_no = int(input("Enter account number: "))
                    account = self.get_account(acc_no)
                    account.print_statement()

                elif choice == 7:
                    acc_no = int(input("Enter account number: "))
                    account = self.get_account(acc_no)
                    account.show_details()

                elif choice == 8:
                    print("Thank you for using the bank. Goodbye!")
                    break

                else:
                    print("Invalid choice. Please select from 1 to 8.")

            except ValueError as ve:
                print(f"Value Error: {ve}")
            except KeyError as ke:
                print(f"Key Error: {ke}")
            except Exception as e:
                print(f"Error: {e}")


# Start the banking application
if __name__ == "__main__":
    bank = Bank()
    bank.run()
