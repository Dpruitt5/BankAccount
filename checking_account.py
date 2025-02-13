from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, recipient):
        if amount < self.transfer_limit:
            print(f"transfer failed! Cannot transfer more than ${self.transfer_limit} at a time")
        elif amount > self.current_balance - self.minimum_balance:
            print("Transfer failed! Insufficient funds.")

        else:
            self.current_balance -= amount
            recipient.current_balance += amount
            print(f"Transferred ${amount} to {recipient.customer_name}. New balance is ${self.current_balance}.")
