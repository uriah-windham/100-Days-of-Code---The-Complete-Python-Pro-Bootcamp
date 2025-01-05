import art

def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(art.logo)
    continue_calculation = True
    first_number = float(input("What is the first number: "))

    while continue_calculation:
        for symbol in operations:
            print(symbol)
        user_operation = input("Pick and operation:\n")
        second_number = float(input("What is the second number: "))
        result = operations[user_operation](first_number, second_number)
        print(f"{first_number} {user_operation} {second_number} = {result}")

        answer = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'end' to end program: ").lower()
        if answer == "y":
            first_number = result
        elif answer == "n":
            continue_calculation = False
            print("\n" * 100)
            calculator()
        else:
            print("Ending program")
            continue_calculation = False

calculator()