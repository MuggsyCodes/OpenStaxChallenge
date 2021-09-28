# Using this script as a test bed for my changes
# Import classes from other files

from questions import Questions
# list of players
from player import available_players
from data import question_list
from score import Score

# module import
from random import randrange

from OER_logo import oer_logo
from art_1 import calvin

# **** START OER GAME ******* # 

def play_oer():
    if __name__ == '__main__':
        not_a_winner = False

        # show OER logo
        print(oer_logo)
        # user promoted to start game
        user_choice_1 = input("Would you like to play OER? ").lower()
        if user_choice_1 == "yes" or "y":
        # instaniate new Question object
            question = Questions()

            ### Manually add players ### 
            #question.add("James")
            #question.add("Enzo")
            #question.add("Woody")

            for player in available_players:
                question.add(player)

            #create list of questions from question bank
            question.question_bank(question_list)

            # new score object
            score = Score()

            while True:
                # roll method requires question object - WHY? #
                question.roll(randrange(0,6), question)

                # report score each time the first player is about to roll
                if question.current_player == 0:
                    # dictionary of player data and names
                    player_dictionary = score.report_score(question.players, question.purses)

                if randrange(9) == 7:
                    not_a_winner = question.wrong_answer()
                else:
                    not_a_winner = question.was_correctly_answered()
                # play game until not_a_winner is False
                if not not_a_winner:
                    #print(f"not a winner state: {not_a_winner}")
                    print(f"{question.players[question.current_player]} Wins the game!")
                    score.score_file(player_dictionary)
                    print(f"Game over - new DataFile created")
                    # print ending logo
                    print(calvin)
                    break # if not True --> break
            # recursive call to begin game again - NOT working as expected
            #play_oer()
        else:
            print("See you later.")

# play game
play_oer()

