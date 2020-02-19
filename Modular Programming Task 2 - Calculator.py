'''Functions'''

#Addition
def add(num1, num2):
    ans = num1+num2
    return ans

#Subtraction
def sub(num1, num2):
    ans = num1-num2
    return ans

#Multiplication
def mul(num1, num2):
    ans = num1*num2
    return ans

#Division
def div(num1, num2):
    ans = num1/num2
    return ans

#Asking for numbers and making them global
def numbers():
    global num1, num2
    num1 = int(input("Okay, what is your first number? "))
    num2 = int(input("What is your second number? "))

def contin():
    global cont
    userChoice = input("Do you want to continue? (Yes or No)  ")
    if userChoice == "Yes":
        cont = True
    elif userChoice == "No":
        cont = False

'''Main Program'''
userName = input("What is your name? ")
print("Welcome to my Calculator,",userName)

cont = True
while cont == True:
    calculation = input("First type the type of calculation (Addition, Subtraction, Multiplication or Division) you want to perform: ")

    if calculation == "Addition":
        numbers()
        print("The answer is", str(add(num1, num2)))
        contin()

    elif calculation == "Subtraction":
        numbers()
        print("The answer is", str(sub(num1, num2)))
        contin()

    elif calculation == "Multiplication":
        numbers()
        print("The answer is", str(mul(num1, num2)))
        contin()

    elif calculation == "Division":
        numbers()
        print("The answer is", str(div(num1, num2)))
        contin()

    else:
        print("Error: Not a type of Calculation! Please select from Addition, Subtraction, Multiplication or Division.")
        contin()
    