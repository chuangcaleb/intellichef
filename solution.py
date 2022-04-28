
import random

suspects = ['green', 'white', 'scarlet', 'plum', 'mustard', 'peacock']
weapons = ['knife', 'pipe', 'rope', 'candlestick', 'gun', 'wrench']
rooms = ['conservatory', 'billiard', 'library', 'study',
         'hall', 'lounge', 'dining', 'kitchen', 'ballroom']


def solution():
    murder_suspect = random.choice(suspects)
    murder_weapon = random.choice(weapons)
    murder_room = random.choice(rooms)
    return (murder_suspect, murder_weapon, murder_room)


print(solution())
# print(murder_suspect)
