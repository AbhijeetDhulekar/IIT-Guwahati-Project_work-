def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    number1=int(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an operation: ")
        number2=int(input("Enter second number: "))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        continue_calculation=input("Enter 'y' to continue to calculation or enter 'n' to start new calculation or 'x' to exit").lower()
        if continue_calculation=='y'
            number1=output
        elif continue_calculation=='n':
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print("Good Bye")
calculator()


