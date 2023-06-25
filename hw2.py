result = 0
operand = None # 0, 1, 2, 3..
operator = None # + - * / 
wait_for_number = True

operator_list = "+-/*"
rule = "="  


while wait_for_number == True:
    operand = input("Enter number: ")
    try:
        operand = int(operand)
    except ValueError:
        print(f"{operand} is not a number. Try again.")
    else: 
        wait_for_number = False

while wait_for_number == False:
    operator = input("Enter operator: ")    
    if operator == '+' or operator == '*' or operator == '/' or operator == '-':
        wait_for_number = True
    else:
        print(f"{operator} is not '+' or '-' or '/' or '*'. Try again") 
if operator == "+":
    result += operand
elif operator == "-":
    result -= operand
elif operator == "*":
    result *= operand
elif operator == "/":
    result /= operand
print(result)