print( '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|



''')
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/":divide,
}

def calculator():
    should_accumulate = True
    num1 =float(input("What's the first number?: "))
    
    while should_accumulate:
        
        
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        
        choice = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")
        
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()