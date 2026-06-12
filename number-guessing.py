secret_number = 20 
assumed_number = 2 
while assumed_number != secret_number :  
    assumed_number = int ( input ( " assume the number ( 1 - 28 ) : " ) )        
    if assumed_number == secret_number  :     
          print ( " Congratulations !!!! " , " You win this game\n " ) 
          break        
    else :    
          print ( " No wrries !!!!. In next attempt, you will do it. Try again  \n" ) 