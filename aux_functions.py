#The user choose a number until he hit the guess

def user_guess(rand_numb):
    guess_numb = 0
    while (guess_numb != rand_numb ):
        guess_numb = int(input('Guess >'))
        if( guess_numb > rand_numb ):
            print('Too high!')
        elif( guess_numb < rand_numb ):
            print('Too low!')
    
    print(f'That is it! You guessed the number >> {guess_numb}')