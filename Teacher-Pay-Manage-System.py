# 1) Cteate Structure ( Class ) :- 
class teachers_salary :
# 2) To need some special things to make an object :- 
    def __init__(self,name,present_day,absent_day,salary) : 
        self.name = name 
        self.present_day = present_day 
        self.absent_day = absent_day 
        self.salary = salary
## 3) 1 diner salary, per day salary  calculate kora :- 
    def salary_info(self) :   
        total_day = self.present_day + self.absent_day 
        per_day_salary = self.salary / total_day
        deserve_salary = per_day_salary * self.present_day   
        return int(deserve_salary)  
# 4) What can create object those special  things :- 
    def teachers_info( self )  : 
        final_salary = self.salary_info() ## ei jaigai return kora jinishta save hochhe 
        print(f"Teacher name is: {self.name}\n" )        
        print(f"{self.name} present day is: {self.present_day}\n") 
        print(f"{self.name} absent day is: {self.absent_day}\n") 
        print(f"{self.name} base salary is: {final_salary}\n")         
# 5) By using the structure (class), create object :- 
teacher_1=teachers_salary("Shahin Akhter",28,2,35000) 
teacher_2=teachers_salary("Nahid Islam",30,0,35000) 
teacher_3=teachers_salary("Asaduzzaman",29,1,35000) 
teacher_4=teachers_salary("Nurul Islam",26,4,35000)
# 6) show the object :-
teacher_1.teachers_info() 
teacher_2.teachers_info() 
teacher_3.teachers_info() 
teacher_4.teachers_info() 