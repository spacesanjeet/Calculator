#building a calculator
while (1==1):          #to make sure that the program runs until the user doesn't choose to quit
    print("Options:")
    print("Type 'add' for the addition of two numbers")
    print("Type 'multiply' for the multiplication of two numbers")
    print("Type 'subtract' for the subtraction of two numbers")
    print("Type 'divide' for the division of two numbers")
    print("Type 'modulo' for the remainder by division of two numbers")
    print("Type 'floor' for the non-decimal value by division of two numbers")
    print("Type 'quit' to end the program")
    user_input = input(": ")
    if user_input == "quit":
        break
    elif user_input == "add":
        num = float(input("Enter a integer: "))
        num_1 = float(input("Enter another integer: "))
        result = str(num + num_1)
        print("The result is " + result)
    elif user_input == "multiply":
        num = float(input("Enter a integer: "))
        num_1 = float(input("Enter another integer: "))
        result = str(num * num_1)
        print("The result is " + result)
    elif user_input == "subtract":
        num = float(input("Enter a integer: "))
        num_1 = float(input("Enter another integer: "))
        result = str(num - num_1)
        print("The result is " + result)
    elif user_input == "divide":
        num = float(input("Enter a integer: "))
        num_1 = float(input("Enter another integer: "))
        try:
            result = str(num / num_1)
            print("The result is " + result)
        except:
            print("Division by zero, can't divide a number by zero!!")
    elif user_input == "modulo":
        num = int(input("Enter a integer: "))
        num_1 = int(input("Enter another integer: "))
        try:
            result = str(num % num_1)
            print("The result is " + result)
        except:
            print("Division by zero, can't find the modulo when divided by zero!!")
    elif user_input == "floor":
        num = int(input("Enter a integer: "))
        num_1 = int(input("Enter another integer: "))
        try:
            result = str(num // num_1)
            print("The result is " + result)
        except:
            print("Division by zero, can't find the floor when divided by zero!!")
    else:
        print("Unknown input")
#program ends!!
