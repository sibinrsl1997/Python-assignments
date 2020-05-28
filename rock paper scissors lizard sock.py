#http://www.codeskulptor.org/#user47_ivYRcl0m6YSluy3.py
import random
# name to number
# 0 — rock
# 1 — Spock
# 2 — paper
# 3 — lizard
# 4 — scissors
def name_to_number(name):
    if name == 'rock':
        y = 0
        return y
    elif name == 'spock':
        y = 1
        return y
    elif name == 'paper':
        y = 2
        return y
    elif name == 'lizard':
        y = 3
        return y
    elif name == 'scissors':
        y = 4
        return y

def number_to_name(x):
    if x == 0:
        c = 'rock'
        return c
    elif x == 1:
        c = 'spock'
        return c
    elif x == 2:
        c = 'paper'
        return c
    elif x == 3:
        c = 'lizard'
        return c
    elif x == 4:
        c = 'scissors'
        return c
def rpsls(player_choice):
    b = player_choice #inputting the player choice
    a = name_to_number(b) #changed to name to number
    print('Player chooses ',b) # printing the input# a is the number for the input choice
    x = random.randint(0,4)
    d = number_to_name(x)#d is the computer choice
    print('Computer choeses ',d)
    # 0 — rock# 1 — Spock# 2 — paper# 3 — lizard# 4 — scissors
    #Rock crushes spock and scissors
    #conditions for rock
    if a == 0 and x == 0:
        print('Player and computer tie!')
    elif a == 0 and x == 1:
        print('Computer wins')
    elif a == 0 and x == 2:
        print('Computer wins')
    elif a == 0 and x == 3:
        print('Player wins')
    elif a == 0 and x == 4:
        print('Player wins')
    # 0 — rock# 1 — Spock# 2 — paper# 3 — lizard# 4 — scissors
    #conditions for spock
    # spock smashes scissor and vaporize rocks
    if a == 1 and x == 1:
        print('Player and computer tie!')
    elif a == 1 and x == 3:
        print('Computer wins')
    elif a == 1 and x == 2:
        print('Computer wins')
    elif a == 1 and x == 4:
        print('Player wins')
    elif a == 1 and x == 0:
        print('Player wins')
    # 0 — rock# 1 — Spock# 2 — paper# 3 — lizard# 4 — scissors
    #conditions for paper
    #paper covers rock and disapproves spock
    if a == 2 and x == 2:
        print('Player and computer tie!')
    elif a == 2 and x == 3:
        print('Computer wins')
    elif a == 2 and x == 4:
        print('Computer wins')
    elif a == 2 and x == 1:
        print('Player wins')
    elif a == 2 and x == 0:
        print('Player wins')
    # 0 — rock# 1 — Spock# 2 — paper# 3 — lizard# 4 — scissors
    #conditions for lizard
    #lizard poisond spock and eats paper
    if a == 3 and x == 3:
        print('Player and computer tie!')
    elif a == 3 and x == 0:
        print('Computer wins')
    elif a == 3 and x == 4:
        print('Computer wins')
    elif a == 3 and x == 1:
        print('Player wins')
    elif a == 3 and x == 2:
        print('Player wins')
    # 0 — rock# 1 — Spock# 2 — paper# 3 — lizard# 4 — scissors
    #conditions for scissors
    #Scissors cuts paper and decapitates lizard
    if a == 4 and x == 4:
        print('Player and computer tie!')
    elif a == 4 and x == 0:
        print('Computer wins')
    elif a == 4 and x == 1:
        print('Computer wins')
    elif a == 4 and x == 3:
        print('Player wins')
    elif a == 4 and x == 2:
        print('Player wins')
print()
rpsls("rock")
print()
rpsls("spock")
print()
rpsls("paper")
print()
rpsls("lizard")
print()
rpsls("scissors")
print()