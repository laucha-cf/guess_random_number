import random
from aux_functions import user_guess as u

def guess( x ):
    rand_numb = random.randint(1, x)
    u(rand_numb)

if __name__ == '__main__':
    num = int(input('Put the top of interval >> '))
    guess( num )


