import time

#python calculator
#does *, +, /, -,


#adds the two numbers
def add(x, y):
    return x + y


#subtracts two numbers
def subtract(x, y):
    return x - y


# multiplies two numbers
def multiply(x, y):
    return x * y


#Divides two numbers
def divide(x, y):
    return x / y

print('''
           _            _       _              
          | |          | |     | |             
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __  
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__| 
| (_| (_| | | (__| |_| | | (_| | || (_) | |    
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|    
  by @FearMyLocus
      ''')



time.sleep(0.5)
print('Which Operation Is Required…?')
time.sleep(0.2)
print('1.) Addition ')
time.sleep(0.3)
print('2.) Subtraction ')
time.sleep(0.4)
print('3.) Multiplication ')
time.sleep(0.5)
print('4.) Division ')

while True:
    #user input what they need
    choice = input("please pick an option 1-4: ")
    if choice in ('1', '2', '3', '4'):
        #OPT short for option
        OPT1 = float(input("Enter first number: "))
        OPT2 = float(input("Enter second number: "))

        if choice == '1':
            print(OPT1, "+", OPT2, "=", add(OPT1, OPT2))

        elif choice == '2':
            print(OPT1, "-", OPT2, "=", subtract(OPT1, OPT2))

        elif choice == '3':
            print(OPT1, "*", OPT2, "=", multiply(OPT1, OPT2))

        elif choice == '4':
            print(OPT1, "/", OPT2, "=", divide(OPT1, OPT2))

        next_calc = input("Let's do another problem? (y/n): ")
        if next_calc != "y":
            break

    else:
        print("oops.. Try again")