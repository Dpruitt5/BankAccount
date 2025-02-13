from savings_account import SavingsAccount
from checking_account import CheckingAccount

# Scenario: A user opens a checking account and performs transactions
print("Creating Accounts...\n")

# Creating a Savings Account
savings = SavingsAccount("david", 5000, 1000, "SA12345", "RT67890", 2.5)
savings.print_customer_information()
savings.apply_interest()
print("\n")

# Creating a Checking Account
checking = CheckingAccount("david2", 3000, 500, "CA54321", "RT67890", 1000)
checking.print_customer_information()
checking.withdraw(200)
checking.transfer(800, savings)
checking.transfer(1200, savings)  # Should fail due to transfer limit
print("\n")

# Final Account Balances
print("Final Account Balances:")
savings.print_customer_information()
checking.print_customer_information()
