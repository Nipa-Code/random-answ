from math import sqrt

def main():
    options = {
        1: sum,
        2: subtraction,
        3: square_root,
        4: multiply,
        5: exponent,
        6: divide,
        7: percent,
        10: info}
    choice = int(input("[1]summ \n[2]Subtraction \n[3]square root\n[4]multiply\n[5]Exponent\n[6]divide\n[7]percent\n"))
    if choice == 3:
        result = options[choice](ask(choice))
        print(result)
    elif choice == 10:
        info()
    else:
        result = options[choice](*ask(choice))
        print(result)
def ask(c):
    if c != 3:
        num1 = int(input("Number: "))
        num2 = int(input("Number: "))
        return num1, num2
    num = int(input('Number: '))
    return num
def sum(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def square_root(n):
    return sqrt(n)
def multiply(num1, num2):
    return  num1 * num2
def exponent(num1, num2):
    return  num1 ** num2
def divide(num1, num2):
    return num1 / num2
def percent(num1,num2):
    return num1 / 100 * num2
    
def info():
    infos = """
    This program is made using Python.
    This was used to learn and test my knowledge of Python
    I guess, I got lot's of things to improve and understand.
    Any ideas? ping me for that
    """
    print(infos)
while True:
    main()