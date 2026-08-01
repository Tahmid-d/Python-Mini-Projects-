class DailyActivity :
    def __init__ (self,name,day_name,steps,calories) :
        self.name=name
        self.day_name=day_name
        self.steps=steps
        self.calories=calories
    def __str__ (self) : ## user ke valo text show korar jonno ei method:-      
        return f"Name: {self.name} | Day: {self.day_name} | Total Steps: {self.steps} | Total Calories: {self.calories}\n" 
    def __len__ (self) : ## object er size calculate korar jonno ei method:- 
        daily_steps=int(self.steps) 
        return daily_steps
    def __eq__ (self,other) : ## object gula same same check korar method:-
        if self.steps==other.steps and self.calories==other.calories :
            return True 
        else :
            return False 
    def __add__ (self,other) : ## object gula summation korar jonno ei method:- 
        new_name=self.name + " & " +other.name
        new_day_name=self.day_name + " & " + other.day_name 
        total_steps=self.steps+other.steps
        total_calories=self.calories+other.calories                                               
        new_daily_activity= DailyActivity(new_name,new_day_name,total_steps,total_calories)     
        return new_daily_activity  
## Create Objects:-                    
day1=DailyActivity("Raboit","Wednesday",40000000,1000) 
day2=DailyActivity("Tchouameni","Friday",1000000,980)  
print(day1==day2) ## call the __eq__ method 
print(day1) ## call the __st__ method
print(len(day1)) ## call the __len__ method
print(day2) ## call the __str__ method 
print(len(day2)) ## call the __len__ method    
weekly_report=day1+day2 
print(weekly_report)   