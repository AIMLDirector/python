class BankAccountInfo():
    def __init__(self, AccountNo:int, Date, Balance:int, Cust_Name):
        self.AccountNo = AccountNo
        self.Date = Date
        self.Balance = Balance
        self.Cust_Name = Cust_Name

    def CustomerInfo(self):
        print("Name:", self.Cust_Name)
        print("AccountNumber:", self.AccountNo)
        print("Date:", self.Date)
        print("Balance:", self.Balance)

    def DepositMoney(self, Money:int):
        self.Balance+= Money
        print(f"{Money} /- has been deposited to your account: {self.AccountNo}")
        print(f"Total Balance: {self.Balance} /- ")


Accountone = BankAccountInfo(100, "10-10-2020", 2000, 'suman')  # redis(DB for in memory information) cache show you the account information 


Accountone.CustomerInfo()
Accountone.DepositMoney(3000)

