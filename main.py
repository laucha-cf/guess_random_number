import random
from aux_functions import *


if __name__ == '__main__':
    option = 0
    while option != 1 and option != 2:
        option = int(input('Guest(1) or Host(2)? >> '))

    num = int(input('Put the top of interval (bottom is 1) >> '))

    if option == 1:
        user_guess( num )
    elif option == 2:
        computer_guess( num )


