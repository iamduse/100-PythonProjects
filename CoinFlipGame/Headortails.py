#using the power of random module we will create head and tail game
import random

head_tail_random = random.randint(a=0,b=1)
tab_randomly = input("choose head or tail ")
if head_tail_random == 0:
    print("Head")
else:
    print('Tails')

