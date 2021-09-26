# Using this script as a test bed for my changes
# Import classes from other files

from questions import Questions
#from player import Player

# module import
from random import randrange

from OER_logo import oer_logo
from art_1 import calvin

# **** START OER GAME ******* # 

def play_oer():
#if __name__ == '__main__':
    not_a_winner = False

    # show OER logo
    print(oer_logo)
    user_choice_1 = input("Would you like to play OER?").lower()
    if user_choice_1 == "yes" or "y":
        # instaniate new Question object
        question = Questions()
        question.add("James")
        question.add("Enzo")
        question.add("Woody")

        while True:
            # roll method requires question object - WHY? #
            question.roll(randrange(0,6), question)

            val = randrange(9)
            if val == 7:
            #if randrange(9) == 7:
                not_a_winner = question.wrong_answer()
            else:
                not_a_winner = question.was_correctly_answered()
            # play game until not_a_winner is False
            if not not_a_winner:
                print(f"not a winner state: {not_a_winner}")
                print(f"Game over") 
                print(calvin)
                break # if not True --> break
    else:
        print("See you later.")
play_oer()

'''What needs to happen exactly? 
* question needs to have reference to newly created player object
'''
