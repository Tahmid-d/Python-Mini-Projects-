## parent class :- 
class normal_customer : 
    def __init__ (self,name,total_bill) : 
        self.name = name
        self.total_bill = total_bill 
    def calculate_bill (self) : 
        print(f" Hey, {self.name} is a normal customer in this shop. So,{self.name} will not get discount.{self.name} total bill is: {self.total_bill}\n") 
## child class :- 
class premium_customer ( normal_customer) : ## Call the normal_customer (parent class) 
    def __init__ (self, name, total_bill) : 
        super(). __init__ (name,total_bill) 
    def calculate_discount (self) : 
        final_bill = self.total_bill - 180    
        return int(final_bill)         
    def calculate_bill (self) :       
        final_bill_2 = self.calculate_discount()
        print(f"Now,{self.name} is a premium customer in this shop.So,{self.name} will get discount.{self.name} final bill is: {final_bill_2} \n") 
customer_1 = normal_customer ("Azad",2180) 
customer_2 = premium_customer ("Nirob",1400) 
customer_3 = normal_customer("Rafiq",1720) 
customer_4 = premium_customer ("Ousmane",880)
customer_1 .calculate_bill() 
customer_2 .calculate_bill()   
customer_3 .calculate_bill()   
customer_4 .calculate_bill()                     