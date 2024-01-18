import random

is_valid_input = False

while not is_valid_input:
    z = input("How many games do you want to play?\nEnter a number smaller than 5 and larger than 0: ")

    try:
        z_int = int(z)
    except ValueError:
        print("That is not a valid number, dumbo")
        continue
    except:
        print("No idea what happened, but I'm gonna say try again")
        continue
    else:
        is_valid_input = True



if z_int < 0 or z_int >= 6:
    print("Do you not understand words?")
elif z_int == 0:
    print("You don't have to be like that.\nWere you not hugged as a child?")



elif z_int >0 and z_int <=5:
    for x in range(z_int):
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
            else:
                print('oops')
        elif player == 'paper':
            if computer == 'rock':
                print('You win!')
            elif computer == 'scissors':
                print('Computer wins')
            else:
                print('oops')
        elif player == 'scissors':
            if computer == 'rock':
                print('Computer wins')
            elif computer == 'paper':
                print('You win!')
            else:
                print('oops')
        else:
            print("Apparently you can't type properly....")

#---------------------------------------------------------------------------#
    
