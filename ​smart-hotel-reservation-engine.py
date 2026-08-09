class HotelReservation :
    def __init__ (self,name,room_category,per_night_fare,total_nights) :
        self.name=name
        self.room_category=room_category
        self.per_night_fare=per_night_fare
        self.total_nights=total_nights
    @staticmethod ## static method use to check the validation 
    def is_valid_promo(promo_code) : 
        promo_code1="FRANCE199" 
        promo_code2="TURKEY11"     
        if promo_code == promo_code1 or promo_code == promo_code2 :
            return True
        else :
            invalid_txt="Invalid Promo Code !!"
            return invalid_txt and  False
    @classmethod ## class method use to 
    def from_booking_string(cls,booking_str) :   
        parts=booking_str.split("-") 
        name=parts[0] 
        room_category=parts[1]
        per_night_fare=int(parts[2])        
        total_nights=int(parts[3]) 
        return cls(name,room_category,per_night_fare,total_nights) ## cls() কল করা মানে হলো HotelReservation() কল করা।  
    def generate_bill(self,opt_promo_code=None) :      
        base_bill=self.per_night_fare*self.total_nights
        
   ## স্ট্যাটিক মেথড দিয়ে প্রোমো কোড চেক করছি!
   ## ক্লাসের নাম ধরে স্ট্যাটিক মেথড কল করতে হয়। 
        if opt_promo_code is not None and HotelReservation.is_valid_promo(opt_promo_code) is True :
            discount= base_bill * 0.15 ## 15% discount 
            final_bill=base_bill-discount
            status="Promo Applied ! 15% OFF."
        else :
            final_bill=base_bill
            status="No Promo Applied !"
        return f"Guest: {self.name} | Room:  {self.room_category} | Bill: ${final_bill} \nStatus: {status}\n" 
##  ১. ক্লাস মেথড ব্যবহার করে ডিরেক্ট স্ট্রিং থেকে অবজেক্ট তৈরি করা:-              
booking1=HotelReservation.from_booking_string ("Van der Sar-Luxurious-3000-3") 
booking2=HotelReservation.from_booking_string("David De Gea-Presidential-5000-4") 
## 2. Check the bill ( without promo code) 
print(booking1.generate_bill())  
print(booking2.generate_bill()) 
print(booking1.generate_bill("INDIA")) ## check the invalid promo code
print(booking1.generate_bill("TURKEY11")) ##  Check the valid promo code for booking1  
print(booking2.generate_bill("FRANCE199")) ##  Check the valid promo code booking2                   