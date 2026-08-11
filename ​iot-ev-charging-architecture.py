class EVChargingStation :
    def __init__ (self,car_model,present_battery,voltage) : 
        self.car_model=car_model
        self.present_battery=present_battery
        self.voltage=voltage
    @staticmethod ## static method use to check the validation 
    def check_safety(present_battery,voltage) : 
         present_battety=int(present_battery)                          
         voltage=int(voltage)
         volt_valid=500 ## voltage limited in 500 
         battery_valid=100 ## battery limited in 100%
         if voltage < volt_valid and present_battery < battery_valid :
             return True 
         else :
             return False 
    @classmethod ## Use class method to design the project
    def parse_sensor_data(cls,sensor_str) :
         parts=sensor_str.split("-") # A string text parts by "-" 
         car_model=parts[0] 
         present_battery=int(parts[1]) 
         voltage=int(parts[2]) 
         return cls(car_model,present_battery,voltage) # Call the class name to create an object which is named (cls) 
    def start_charging(self) :                
        if EVChargingStation.check_safety(self.present_battery,self.voltage) is False : # validation check and call the check_safety method 
            warning_txt="Safety Warning: Cannot charge this vehicle!!\n"             
            return warning_txt              
        else :
   # calculate math for line:(29-32)           
            remain_battery=100-self.present_battery     
            total_time=remain_battery*1.5
            every_charge_dollar=3        
            total_cost=remain_battery*every_charge_dollar   
        return f"Car Model: {self.car_model} | Target: 100% | Time Required: {total_time} mins |\n Total Battery: {self.present_battery}% | Total Voltage: {self.voltage} \n Total Cost: ${total_cost}\n." 
## Testing Objects :–
ev1=EVChargingStation.parse_sensor_data("BYD56X1-95-490")
ev2=EVChargingStation.parse_sensor_data("TESLA[9x]-87-405")
print(ev1.start_charging()) # call the start_charging method   
print(ev2.start_charging()) # call the start charging method    