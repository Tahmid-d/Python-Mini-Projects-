print ( f"simple calculator game \n")
print ( f"let is start............\n") 

# লুপটি একদম শুরুতেই দেওয়া হলো যেন প্রতিবার নতুন ইনপুট নেয়     
for attempt in range(1,6) : 
    print(f" Attempts {attempt} of 5 \n") 
      # ইনপুটগুলো লুপের ভেতরে নিয়ে আসা হলো     
    num1 = float (input( "Enter the first number:    "))
    num2 = float (input("Enter the second number:   ")) 
    print( "1. Addition")
    print( "2. Substraction")
    print( "3. Multiple")
    print( "4. Divide")     
    choice = input ( " choose 1/2/3/4 \n") 
    if choice == "1" : 
        print ( " Answer : ", num1+num2)
    elif choice == "2" : 
        print ( " Answer : ", num1-num2) 
    elif choice == "3" : 
        print ( " Answer : ", num1*num2)
    elif choice == "4" :         
        if num2 != 0 : 
            print ( " Answer : ", num1/num2)     
        else : 
            print (f" any number do not divided by 0 or ZERO \n") 
    else : 
        print(f" Invalid choice. please correct chooice \n")
print(f"Game Over! You have used all your 5 attempts.\n")                                                    