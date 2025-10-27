print ('Please enter a number:')
number1 = float(input())

print ('Please enter another number:')
number2 = float(input())

print('please select an operation for these two numbers:\n'
        '1. Addition\n'
        '2. Subtration\n'
        '3. Multiplication\n'
        '4. Division\n')

operation = input()
possible_opertations = [1,2,3,4]
#I created an array of numbers so edge case numbers or characters will be compared later and return an invalid input
number3 = 0
#number3 is declare as a variable but is intended to be overwritten

if operation == 1:
    operation = '+'
    number3 = number1 + number2
    
elif operation == 2:
    opertation = '-'
    number3 = number1 - number2 

elif operation == 3:
    operation = '*'
    number3 = number1 * number2 
    
elif operation == 4:
    operation = '/'
    if number2 != 0:
        number3 = number1 / number2

if number2 == 0:
    print('Error, you cannot divide by zero')
    

if operation != [1,2,3,4]:
    print('Invalid input')
    
    

print(f'{float(number1)} {operation} {float(number2)} is = {number3}')
