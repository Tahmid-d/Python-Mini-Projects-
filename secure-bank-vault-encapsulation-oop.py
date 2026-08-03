class BankVault :
    def __init__ (self,holder_name,initial_balance,total_deposit,total_withdraw) : ## constructor 
        self.holder_name=holder_name
        self.__initial_balance=initial_balance ## private variable 
        self.__total_deposit=0 ## private variable
        self.__total_withdraw=0 ## private variable 
    def deposit_balance (self,amount) : ## taka save korar method 
        if self.__initial_balance > 0 :
            self.__initial_balance += amount
            self.__total_deposit += amount
            return f"Update Balance: ${self.__initial_balance} \nDeposit Balance: ${self.__total_deposit}.Deposit Successful.\n"
        else :
            return f"Invalid Deposit Balance!!!"
    def withdraw (self,amount) : ## taka tule naoar method 
        if self.__initial_balance > 0 and self.__initial_balance >= amount :
            self.__initial_balance -= amount
            self.__total_withdraw += amount
            return f"Update Balance: ${self.__initial_balance} \nWithdraw Balance: ${self.__total_withdraw}.Withdrwal Successful\n"     
        else :
            return f"Withdrawal Balance Insufficient!!\n" 
    def __str__ (self) : ## Dunder method
        return f"=== ACCOUNT STATEMENT ===  Account Holder: {self.holder_name} \nCurrent Balance: ${self.__initial_balance} | Total Deposited: ${self.__total_deposit} | Total Withdrawn: ${self.__total_withdraw}\n"
    def get_balance (self) : ## getter method (Encapsulation) 
        return self.__initial_balance
        return self.__total_withdraw
        return self.__total_deposit        
## Create Objects:-
holder1=BankVault ("Courtois",30000,0,0) 
print(holder1.deposit_balance(15000)) ## call the deposit_balance method
print(holder1.withdraw(20000)) ## call the withdraw method 
print(holder1) ## call the __str__ method
holder1.__initial_balance=-100000 ## To destroy initial balance (example:30000) 
holder2=BankVault ("Nueur",40000,0,0)  
print(holder2.deposit_balance(8000)) ## call the desposit_balance method
print(holder2.withdraw(19000)) ## call the withdraw method
print(holder2) ## call the __str__ method         