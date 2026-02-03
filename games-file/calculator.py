def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

while True:
    print("Select")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    print("Q to Quit")
    choice = input("").strip()
    if choice.lower() =='q':
        break
    try:
        n1 = int(input("Enter number 1: "))
        n2 = int(input("Enter number 2: "))
    except ValueError:
        print("Please enter numbers")
        continue
    match choice:
        case '+':
            print(add(n1,n2))
        case '-':
            print(subtract(n1,n2))
        case '*':
            print(multiply(n1,n2))
        case '/':
            if n2!=0:
                print(divide(n1,n2))
            else:
                print("Cannot divide by 0")
        case _:
            print("Choose from the given options")