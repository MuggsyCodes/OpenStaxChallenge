#!/usr/bin/env python3

class Game:
    def __init__(self):
        self.players = [] ## Player class ##
        self.places = [0] * 6 # corresponds to location # list of length 6 - why? 
        self.purses = [0] * 6 # this is the gold coins score
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0 ## Player class ##
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    def create_rock_question(self, index):
        return "Rock Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2

    ## Player class ##
    def add(self, player_name):
        self.players.append(player_name)

        # *** this appears to be redundant because it replaces 0 with 0 *** #
        #self.places[self.how_many_players] = 0 # what exactly is going on here? # not understanding how_many_players property
        
        # *** this appears to be redundant because it replaces 0 with 0 *** #
        #self.purses[self.how_many_players] = 0 
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(self.players[self.current_player] + \
                            '\'s new location is ' + \
                            str(self.places[self.current_player]))
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player]))
            print("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                    ' now has ' + \
                    str(self.purses[self.current_player]) + \
                    ' Gold Coins.')

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True



        else:

            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


from random import randrange

''' *** Begin game play ***
ORIGINAL game play: Game begins by rolling a random number
# A fixed number of players are added --> Players immediately begin rolling --> Questions from different
categories are randomly assigned --> Questions from a category randomly assigned 
How to win: Player collects 6 gold coins
'''

'''What needs to be improved:
* The game play is disjointed - makes sense to structure the game a bit so that the user knows what's happening. 
* The following are also needed: 
* Gold coins score - dictionary (Player: [score_list])
* Player location - dictionary (Player: [user_location])
* Penalty box status - probably a boolean 
* List of questions - interaction with API question bank would be cool 
* Removing questions from list 
'''

'''Ways to improve the game: 
* Prompting the user to add players randomly
- selected from the list
* Create additional discrete classes: Player, Roll, Score, Question
* A sweet ASCII gui with the OER name

'''

''' ***************** My sausage making process *****************
0. Understand how the game is played in reverse 
1. What is required to win the game? - 6 gold coins by any player
2. How does a player collect gold coins? - by giving correct answers to questions
3. Game play aspects I don't understand now: 
 - what do the places have to do with it? 
 - what does the penalty box have to do with it? 
 - why are there six values in the places, purses (score) and penalty box lists? 
'''



# 1. TODO: Create Player Class in a separte file
# Why classes: makes it easier to modify the main parts of the game 
# Plan is to: add players randomly from a list instead of just a static set of names


if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        #adding watch variable to track places list
        p_places = game.places

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
        # play game until not_a_winner is false
        if not not_a_winner: break # if not True --> break
