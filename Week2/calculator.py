
while True:
    try:
        print ('Please enter a number:')
        number1 = float(input())
        break   
    except ValueError:
        print('Incorrect input, please try a number')
        
while True:     
   try:
       print('Please input a second number')
       number2 = float(input())
       break
   except:
       print('Incorrect input, please try a number')



while True:
    try:
        print('please select an operation for these two numbers:\n'
        '1. Addition\n'
        '2. Subtration\n'
        '3. Multiplication\n'
        '4. Division\n')
        operation = int(input())
        if operation in [1,2,3,4]:
            break
        else:
            print('Incorrect input, please try one of the selections.')
    except ValueError:
        print('Incorrect input, please try one of the selections.')



number3 = None
#number3 is declare as a variable, intended to be overwritten

while True:
    try:
        if operation == 1:
            operation = '+'
            number3 = number1 + number2
            break
    
        elif operation == 2:
            opertation = '-'
            number3 = number1 - number2 
            break
        elif operation == 3:
            operation = '*'
            number3 = number1 * number2
            break
                
        elif operation == 4:
            operation = '/'
            if number2 != 0:
                number3 = number1 / number2
            if number2 == 0:
                print('Cannot divide by 0')
                break
    except:
        if number2 == 0:
                print('Cannot divide by 0')
                
print(f'{float(number1)} {operation} {float(number2)} is = {number3}')
