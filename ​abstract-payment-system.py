from abc import ABC ,abstractmethod 
## Parent Class :- 
class PaymentGetWay (ABC) : 
    @abstractmethod 
    def payment_process (self,amount) : 
        pass 
    @abstractmethod 
    def refund (self,amount) : 
        pass 
## Child Class 1 :- 
class Bkash (PaymentGetWay) : 
    def __init__ (self,name,phone_number) :
        self.name = name 
        self.phone_number = phone_number
    def payment_process (self,amount) : 
        print(f"Customer name: {self.name} | Contact number: {self.phone_number} \n [BKASH] Paid ${amount} successfully from {self.phone_number}\n")  
    def refund (self,amount) : 
        print(f"Customer name: {self.name} | Contact number: {self.phone_number} \n [BKASH] Refunded ${amount} to {self.phone_number}\n ") 
## Child Class 2:- 
class Nagad (PaymentGetWay) : 
    def __init__ (self,name,phone_number) :
         self.name = name 
         self.phone_number = phone_number
    def payment_process (self,amount) : 
         print(f"Customer name is: {self.name} | Contact number: {self.phone_number} \n [NAGAD] Paid ${amount} successfully from {self.phone_number}\n") 
    def refund (self,amount) : 
         print(f"Customer name is: {self.name} | Contact number: {self.phone_number} \n [NAGAD] Refunded ${amount} to {self.phone_number}\n") 
## Testing Objects :- 
bkash_1 = Bkash ("Lamine Yamal","0176556690") 
nagad_1 = Nagad ("Pedro Porro","01772884398") 
bkash_1.refund(7000) 
nagad_1.payment_process(4500)      