class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        # Private attributes
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        elif amount > self.__account_balance:
            return "Insufficient funds for withdrawal."
        else:
            return "Invalid withdrawal amount. Amount must be greater than 0."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"


# Get user input to create a BankAccount instance
account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

# Create an instance of the BankAccount class
account = BankAccount(account_number, account_holder_name, initial_balance)

# Test deposit and withdrawal functionality
print(account.display_balance())  # Display initial balance
deposit_amount = float(input("Enter the amount to deposit: "))
print(account.deposit(deposit_amount))  # Deposit the specified amount
withdraw_amount = float(input("Enter the amount to withdraw: "))
print(account.withdraw(withdraw_amount))  # Withdraw the specified amount
