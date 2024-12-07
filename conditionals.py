day_of_week = input("Enter the day of week: ").lower()
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
       print("i will learn live Devops")
else: 
       print("i will pracetice Devops")

       num1 =int(input("enter first number"))
       num2 =int(input("enter second number"))

       choice = input("enter the opration:(options + , - , * , / , %)")

       if choice =="+":
              sum_of_num =num1 + num2
              print("addition: ",sum_of_num)
       elif choice =="-":
             diff_of_num = num1 - num2
             print("subtraction: ",diff_of_num)
       elif choice == "*":
             prod_of_num =num1 * num2
             print("multiplication: ",prod_of_num)
       elif choice == "/":
              div_of_num = num1 /num2
              print("division: ",div_of_num)
       elif choice == "%":
              rem_of_num = num1 % num2
              print("remainder: ",rem_of_num)
       else:
              print("invalid choice")