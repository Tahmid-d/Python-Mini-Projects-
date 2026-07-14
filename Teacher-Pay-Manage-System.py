# 1) Cteate Structure ( Class ) :- 
class teachers_salary :
# 2) To need some special things to make an object :- 
    def __init__(self,name,present_day,absent_day,salary) : 
        self.name = name 
        self.present_day = present_day 
        self.absent_day = absent_day 
        self.salary = salary 
# 3) What can create object those special  things :- 
    def teachers_info( self )  : 
        print(f" Teacher name is:{self.name},{self.name} present day is:{self.present_day},{self.name} absent day is:{self.absent_day} and his monthly salary is:{self.salary} \n ")   
# 4) By using the structure (class), create object :- 
teacher_1=teachers_salary("Shahin Akhter","28","2","32000") 
teacher_2=teachers_salary("Nahid Islam","30","0","35000") 
teacher_3=teachers_salary("Asaduzzaman","29","1","33820") 
# 5) show the object :-
teacher_1.teachers_info() 
teacher_2.teachers_info() 
teacher_3.teachers_info() 