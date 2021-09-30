# Run this file to play the game 
# I have been using this script as a test bed for my changes
# Import classes from other files

from questions import Questions
# import list of players
from player import available_players
# import list of 48 questions retrieved from API
from data import question_list
# import Score class
from score import Score

from random import randrange

# import sweet ASCII art
from OER_logo import oer_logo, oer_logo_2
from art_1 import calvin

# **** START OER GAME ******* # 

def play_oer():
    if __name__ == '__main__':
        not_a_winner = False
        # set boolean for outside while loop that will dictate continuation of game play or not
        running = True
        # while loop that will continue once game ends or be broken with a user choice of no
        while running:
            # show OER logo
            print(oer_logo)
            print(oer_logo_2)
            # user promoted to start game
            user_choice_1 = input("Would you like to play OER? ").lower()
            if user_choice_1 == "y":
                #not_a_winner = False
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

                running = True
                while running:
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
            else:
                print("Ending the game.")
                running = False

# play game
play_oer()

