class User : 
    def __init__ (self, name, email) : 
        self.name = name 
        self.email = email 
    def login (self) : 
        print(f" User name is:{self.name}. {self.name} email is: {self.email} and {self.name} has logged successfully \n")
class Student (User) : 
    def __init__ (self, name, email, roll_no) : 
        super(). __init__ (name,email) 
        self.roll_no = roll_no         
    def display_student (self) : 
        print(f" Student name is: {self.name}. {self.name} email is: {self.email} and {self.name} roll is:{self.roll_no} \n") 
student_1 = Student("Tahmid","jilaniislam@11gmail.com","20") 
student_2 = Student("Ahmed","ferdous@gmail.com","14") 
student_3 = Student("Mahmud","tahsin@999gmail.com","8") 
student_1.login() 
student_2.login()
student_3.login() 
student_1.display_student()
student_2.display_student()
student_3.display_student()  
