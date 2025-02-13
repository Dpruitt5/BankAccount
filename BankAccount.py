class BankAccount:
    bank_title = "davids Bank"

    def __init__ (self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = int(current_balance)
        self.minimum_balance = int(minimum_balance)
        self._account_number = account_number #protected
        self.__routing_number = routing_number  # Private

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"deposited ${amount}. New balance is ${self.current_balance}")
        else:
            print(f"Must deposit a amount greater than 0")

    def withdraw(self, amount):
        if amount > 0:
            if self.current_balance - amount >= self.minimum_balance:
                self.current_balance -= amount
                print(f"withdrawn ${amount}. New balance is ${self.current_balance}")
            else:
                print(f"you don't have enough money to withdraw")
        else:
            print(f"Must withdraw a amount greater than 0")
    def print_customer_information(self):
        print(f"bank name: {self.bank_title}")
        print(f"customer name: {self.customer_name}")
        print(f"current balance: {self.current_balance}")
        print(f"Minimum balance: {self.minimum_balance}")
        print(f"Account Number: {self._account_number}")  # Accessible in subclass
        print(f"Routing Number: {self.__routing_number}")  # Not directly accessible outside


#instaces
"""account1 = BankAccount("David", "20000", 10000)
account2 = BankAccount("john", "1000", 50)

#testers
account1.print_customer_information()
account1.deposit(1000)
account1.withdraw(100)

print("\n")#spacer to make it look pretty

account2.print_customer_information()
account2.deposit(200)
account2.withdraw(50) 
"""
