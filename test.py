# Using this script as a test bed for my changes
# Import classes from other files

from questions import Questions
#from player import Player

# module import
from random import randrange

# **** START OER GAME ******* # 

if __name__ == '__main__':
    not_a_winner = False

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
            break # if not True --> break


'''What needs to happen exactly? 
* question needs to have reference to newly created player object
'''

'''# probably just call the game here instead of look for main
if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    # for players on list ... add function
    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        # REFACTOR: 
        game.roll(randrange(0,6)) #0 to 5
        #game.roll(randrange(5) + 1) # why +1?

        #adding watch variable to track places list
        # each players location - matches player index
        val = randrange(9)
        if val == 7:
        #if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
        # play game until not_a_winner is False
        if not not_a_winner: break # if not True --> break'''