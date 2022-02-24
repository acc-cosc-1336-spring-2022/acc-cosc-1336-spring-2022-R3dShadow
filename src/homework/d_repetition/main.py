import repetition
choice = int(input("Homework 3 Menu\n1-Factorial\n2-Sum Odd Numbers\n3-Exit\n Select an option above"))

if(choice == 1):
    input = int(input('Input a number between 1 and 10: '))
    if (input < 0 or input > 10):
        print('Enter a valid number.')
    else:
        print('Your factorial is ' + str(repetition.get_factorial(input)))

if(choice == 2):
    input = int(input('Input a number between 1 and 100: '))
    if (input < 0 or input > 100):
        print('Enter a valid number.')
    else:
        print('Your total is ' + str(repetition.sum_odd_numbers(input)))

if(choice == 3):
    print('Menu is exiting.')
