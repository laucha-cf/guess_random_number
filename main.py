import random
from aux_functions import *

def guess( x ):
    rand_numb = random.randint(1, x)
    user_guess(rand_numb)


if __name__ == '__main__':
    option = 0
    while option != 1 and option != 2:
        option = int(input('Guest(1) or Host(2)? >> '))

    if option == 1:
        num = int(input('Put the top of interval >> '))
        guess( num )
    elif option == 2:
        num = int(input('Put the top of interval >> '))
        computer_guess( num )


