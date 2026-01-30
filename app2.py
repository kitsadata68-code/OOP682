from models.bankAccount import BankAccount 


my_account = BankAccount("123456789", "John Doe", 1000.00)
my_account.deposit(500.00)
my_account.withdraw(200.00)
print(my_account)
