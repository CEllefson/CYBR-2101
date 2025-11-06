#Input Validation for first question, realistically should be turned into a defined function for several iterations.
while True:
    try:
        print('Are you enjoying school this year?\n'
        'Please enter y/N:')
        user1 = input().lower()
        if user1 == 'y':
            print("I'm glad you feel that way!")
            break
        elif user1 == 'n':
            print('I hope things turn around for you, reach out to the people around you and things can get better!')
            break
        
        else:
            if user1 != ['y', 'n']:
                print('Invalid input, please try again')
            continue
    
    except ValueError:
        print('Incorrect Response, please try again')

#input Validation Question 2, this one being numeric 1-10        
while True:
    try:
        print('On a scale of 1-10, 1 being the worst and 10 being the best, how would you rate you feelings on this year for school?\n'
        'Please input 1-10:')
        user2 = int(input())
        #alternatively could use:
        #if user2 in list(range(1,11)), this would be better for longer lists using range's (start, stop, step) paramenters, step is defaulted to 1
        if user2 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            break
        
    except ValueError:
        print('Invalid input, please try again')
        continue



#Question 2 input logic and output
while True:
    try:
        if user2 in [1, 2, 3]:
            print("I'm sorry to hear things aren't going well, there are several resources available through the school, and your friends would likely be able to help!")
            break
        elif user2 in [4, 5, 6, 7]:
            print("That's good but things could be better right? Try to think about things you can do to improve your situation and how the resources available can help. Reaching out can always improve your situation!")
            break
        elif user2 in [8, 9, 10]:
            print("That's great! Since things are going great for you, please think of ways to help others who aren't doing as well!")
            break
        else:
            print('Invalid input, please try again')
            
    except ValueError:
        print('Try again')
