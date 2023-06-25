#my first lesson
#is_nice = True
#state = "nice" if is_nice else "not nice"
#print(state)

#temp = input("Enter your name: ")
#name = temp if temp else "Anonimus"
#print(f"Hi, {name}!")

#money = int(input("enter your many: "))
#count_money = money if money else "No money"
#print(f"Dear {name}, you have {count_money}")

fruit = 'apple'
for char in fruit:
    print(char)

num = 1
while num <= 5:
    print(num)
    num += 1

a = 0
while True:
    if a >= 20:
        break
    print(a)
    a = a + 1
while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break
while True:
    number = input("number = ")
    number = int(number)
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break



