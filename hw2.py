result = 0
operand = None # 0, 1, 2, 3..
operator = None # + - * / 
wait_for_number = True

while operator != "=":

    while wait_for_number == True:
        enter_operand = input("Enter number: ") 
        
        try:
         operand = int(enter_operand)
        except ValueError:
            print(f"{operand} is not a number. Try again.")
        else: 
            wait_for_number = False 
            continue       
        
    print(f"Pre Result: {result}")

    while wait_for_number == False:
        operator = input("Enter operator: ")    
        if operator == '+' or operator == '*' or operator == '/' or operator == '-'or operator == "=":
         wait_for_number = True
        else:
         print(f"{operator} is not '+' or '-' or '/' or '*'. Try again") 
         continue
    if operator == "+":
        result += operand
        print(f"Pre Result: {result}")
    elif operator == "-":
        result -= operand
        print(f"Pre Result: {result}")
    elif operator == "*":
        result *= operand
        print(f"Pre Result: {result}")
    elif operator == "/":
        result /= operand
        print(f"Pre Result: {result}")
    elif operator == "=":
    
       print(f"Result: {result}")
       break
    


 #Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
 #Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0   