result = None
operand = None # 0, 1, 2, 3..
operator = None # + - * / 
wait_for_number = True

operator_list = ["+", "-", "/", "*"]
rule = "="


#while type(operand) == int:

while wait_for_number == True:
    operand = input("Enter number: ")
    try:
        operand = int(operand)
    except ValueError:
        print(f"{operand} is not a number. Try again.")
    else: #Цей код виконається, тільки якщо винятків не сталося.
        wait_for_number = False        

    
    
    




