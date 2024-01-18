import random
# Get all my imports

a = 0
is_valid_input = False
score = 0
# set my global variables

while not is_valid_input:
    b = input("How many games do you want to play?")
    try:
        b_int = int(b)
    except ValueError:
        print("That is not a valid number ")
        continue
    except:
        print("No idea what happened, but I'm gonna say try again")
        continue
    else:
        is_valid_input = True
# make all my exceptions for "those people"

    while a < b_int:
        player = input('Player 1 choose rock, paper or scissors: ').lower()
        b_list = ['rock','paper','scissors']
        computer = random.choice(b_list)
        print(f"Computer chooses {computer}")
        print("Go!")
        if player == computer:
            print('TIE')
        elif player == 'rock':
            if computer == 'paper':
                print('Computer wins')
            elif computer == 'scissors':
                print('You win!')
                score += 1
        elif player == 'paper':
            if computer == 'rock':
                print('You win!')
                score += 1
            elif computer == 'scissors':
                print('Computer wins')
        elif player == 'scissors':
            if computer == 'rock':
                print('Computer wins')
            elif computer == 'paper':
                print('You win!')
                score += 1
# the actual game
        else:
            print("Apparently you can't type properly....")
# kinda rude, but necessary
        a += 1
# NO INFINITE LOOPS
        if a == 5:
            print("Ok that's enough.... Go outside and play ")
            break
# Too much gaming, 1984
print(f"Your score is {score} out of {b_int} matches!")
# keep score