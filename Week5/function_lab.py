# Decided to create a restart function instead of copy+pasting the same code 3 or 4 times
def tryAgain(x):
    while True:
        decision = input(x).lower()
        if decision in ['y', 'n']:
            return decision
        print('Please enter Y or N if you would like to do more')

# Fibonacci sequence, one argument 
def fib(x):
    fib = [0,1]

    
    # This just measures the fib list and if it is smaller than the input it will continue with the operation, adding the last two and appending to list fib.
    while len(fib) < x:
        fib.append(fib[-1] + fib[-2])
    #I also tried to see if I could work this out with scientific notation after 100 in len(fib) but I was getting too many errors. it is possible but not within the amount of time I'm willing to spend. Limitations are ok, program can go close to len(fib) 15000, which is more than enough
    
    #printing list slicing ended up being the cleanest way to present the list    
    print(fib[:x])


# Mathmatical approach to determining if a number is a palindrome
def palindromeCheck(x):
    # Stores input number for comparison at end of function
    originalNum = x
    
    
    # Initializes reverseNum
    reverseNum = 0
    while x > 0:
        
        lastNum = x % 10 # Modding by 10 will give you the last digit, let me know if this is too many comments, I prefer to write none unless it becomes verbose
        
        reverseNum = (reverseNum * 10) + lastNum # This appends the number to reverseNum
        
        x = x // 10 # This acts as a counter of iterations


    # Simple comparison of original number input versus the revese number created. If 123 was input, reverseNum will be 321 which is not a palindrome. It's easier to do this through string slicing but since strings are immutable I believe this is technically faster. 
    print(f'**Original Number: {originalNum}, Reversed Number: {reverseNum}')
    if originalNum == reverseNum:
        print(f'***Int number is a palindrome')
    else:
        print('***Int number is not a palindrome')

# Having a hard time thinking of any other functions that have 3 arguments.
def volume(length, width, height):
    volume = length * width * height
    print(f'The Volume is: {volume}')

while True:
    try:
        while True:
            try:
                user1 = int(input('Please input a length for a fibonacci sequence in integer form.\n'
                '***Note-program will break after 20000:  '))
                fib(user1)
                #Input Validation/restart request
                
                decision1 = tryAgain('Would you like to check another number sequence? y/N:\n')
                if decision1 in ['y', 'n']:
                    if decision1 == 'y':
                        continue
                    elif decision1 == 'n':
                        break
            except ValueError:
                continue
            
        while True: 
            try:
                
                #you can use the same variable for all user inputs, but I'm doing it for better delineation
                user2 = int(input('If there is a number you would like to see is a palindrome, being the same number written in reverse, please type it in integer form: '))
                palindromeCheck(user2)
                
                #Input Validation/restart request
                decision2 = tryAgain('Would you like to check another number? y/N:\n')
                if decision2 in ['y', 'n']:
                    if decision2 == 'y':
                        continue
                    elif decision2 == 'n':
                        break    
            except ValueError:
                continue
        while True:
            try:
                print('For the final function, we will be calculating the volume of shape.')
                length = int(input('Please input an integer length:  '))
                width = int(input('Please input an integer width:  '))
                height = int(input('Please input an integer height:  '))
                volume(length, width, height)

                #Input Validation/restart request
                decision3 = tryAgain('Would you like to check another volume? y/N:\n')
                if decision3 in ['y', 'n']:
                    if decision3 == 'y':
                        continue
                    elif decision3 == 'n':
                        print('Thank you, have a good day!')
                        quit()
            except ValueError:
                continue     

    except ValueError:
        print('Invalid input, please try again.')
