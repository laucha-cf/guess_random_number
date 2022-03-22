#The user choose a number until he hit the guess

import random

def user_guess( top ):
    rand_numb = random.randint(1, top)
    
    guess_numb = 0
    while (guess_numb != rand_numb ):
        guess_numb = int(input('Guess >'))
        if( guess_numb > rand_numb ):
            print('Too high!')
        elif( guess_numb < rand_numb ):
            print('Too low!')
    
    print(f'That is it! You guessed the number >> {guess_numb}')

def computer_guess( top ):
    bottom = 1
    feedback = ''
    while feedback != 'c':
        if bottom < top:
            pc_guess = random.randint( bottom, top )
        else:
            pc_guess = bottom
            break
            
        feedback = input(f'Is {pc_guess} too High(H), too Low(L) or correct(C): ').lower()
        if feedback != 'c':
            if feedback == 'h':
                top = pc_guess - 1
            elif feedback == 'l':
                bottom = pc_guess + 1
            print(f'BETWEEN {bottom} and {top}')
            
    print(f'You guessed, genius. The number is {pc_guess}. Anyway, you are a computer')
    
