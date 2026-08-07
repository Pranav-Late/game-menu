def decimal_binary():
    decimal = int(input("Enter a decimal number: "))
    x = 0 
    y = ""
    if decimal == 0:
        print(f'Binary number = 0')
        return
    while decimal > 0:
        x = decimal % 2 
        y += str(x)
        decimal //= 2
    binary = y[::-1]
    print(f'Binary number = {binary}')
    

def decimal_octal():
    decimal = int(input("Enter a decimal number: "))
    x = 0 
    y = ""
    if decimal == 0:
        print(f'Octal number = 0')
        return
    while decimal > 0:
        x = decimal % 8 
        y += str(x)
        decimal //= 8
    octal = y[::-1]
    print(f'Octal number = {octal}')

def decimal_hexadecimal():
    decimal = int(input("Enter a decimal number: "))
    x = 0 
    y = ""
    if decimal == 0:
        print(f'Hexadecimal number = 0')
        return
    while decimal > 0:
        x = decimal % 16
        match x:
            case 10:
                x = "A"
            case 11:
                x = "B"
            case 12:
                x = "C"
            case 13:
                x = "D"
            case 14:
                x = "E"
            case 15:
                x = "F"
        y += str(x)
        decimal //= 16
    hexadecimal = y[::-1]
    print(f'Hexadecimal number = {hexadecimal}')

def binary_decimal():
    binary = int(input("Enter binary number: "))
    decimal = 0
    power = 1

    while binary > 0:
        digit = binary % 10
        decimal += digit * power
        power *= 2
        binary //= 10

    print(f'Decimal number = {decimal}')

print("Welcome to Number Base Convertor")
while True:
    print("Select")
    print("1 to convert from Binary to Decimal")
    print("2 to convert from Decimal to Binary")
    print("3 to convert from Decimal to Octal")
    print("4 to convert from Decimal to Hexadecimal")
    print("5 to Quit")
    choice = int(input(""))
    match choice:
        case 1:
            binary_decimal()
        case 2:
            decimal_binary()
        case 3:
            decimal_octal()
        case 4:
            decimal_hexadecimal()
        case 5:
            break
        case _:
            print("Select from 1 to 5")