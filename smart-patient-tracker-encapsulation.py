class Patient_Record : 
    def __init__ (self,patient_name,heart_rate) : 
        self.patient_name = patient_name
        self.__heart_rate = heart_rate ## private variable         
    def get_heart_rate (self) : ## getter method create     
         print(f"Patient name is:{self.patient_name}. {self.patient_name} heart rate is:{self.__heart_rate}\n") 
         return self.__heart_rate 
    def set_heart_rate (self, new_heart_rate) : ## setter method create and new parameter – new_heart_rate
        ## condition check ( if,else) 
        if new_heart_rate > 40 and new_heart_rate <= 200 :
            self.__heart_rate = new_heart_rate 
        else : 
            print(f"Invalid Heart Rate! Data tampering blocked\n") 
        print(f"Patient name is:{self.patient_name}.{self.patient_name} heart rate is:{self.__heart_rate}") 
 ## 
patient_1 = Patient_Record("Rokeya",80) 
patient_2 = Patient_Record("Rahim",200) 
patient_3 = Patient_Record("Azam",-10) 
patient_4 = Patient_Record("Fatin",340) 
patient_1.set_heart_rate(310) 
patient_2 .set_heart_rate(49)   
patient_3 .get_heart_rate()  
patient_4 .set_heart_rate(65)                                                                