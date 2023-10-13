balance = 0


class Account():
    def __init__(self, balance = 0):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

def main():
    my_account = Account(10)
    print(my_account.balance)
    my_account.deposit(1000)
    my_account.withdraw(500)
    print(my_account.balance)

# def print_balance():
#     print(f"Your balance is: {balance}")

# def withdraw(amount):
#     global balance
#     balance -= amount

# def deposit(amount):
#     global balance
#     balance += amount

if __name__ == '__main__':
    main()