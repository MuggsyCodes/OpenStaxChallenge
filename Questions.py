from player import Player

# How to access player object attributes within the question class?

class Questions(Player):

    def __init__(self):
        # Questions inherits from Player
        super().__init__()
        self.pop_questions = [] #* Question Class *#
        self.science_questions = [] 
        self.sports_questions = []
        self.rock_questions = []

        # game is initiated with 50 dummy questions in each category
        # this could also be done talking to a site via an API
        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    # why was this done separately? 
    # this could be done for all questions
    def create_rock_question(self, index):
        return "Rock Question %s" % index


    # The player's location determines the selected category
    # Definitey can use switch statement here
    # Why? Because all if statements have to be evaluated each time which is inefficient

    # use the switch method - argument current player location (self.places[self.current_player])
    # thank you Dennis
    def switcher(self, argument):
        category_switcher = {
            0: 'Pop',
            4: 'Pop',
            8: 'Pop',
            1: 'Science',
            5: 'Science',
            9: 'Science',
            2: 'Sports',
            6: 'Sports',
            10: 'Sports',
        }

        category = category_switcher.get(argument, 'Rock')
        print(f"Chosen category: {category}")


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

    # Questions class #
    # Definitey can use switch statement here
    # Why? Because all if statements have to be evaluated each time which is inefficient
    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))


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
            # REFACTOR: needs spelling update
            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            # if last player is reached, then start over with first player
            if self.current_player == len(self.players): self.current_player = 0

            return winner
    
    '''
    def was_correctly_answered(self):
        # if current player in penalty box
        if player_obj.in_penalty_box[player_obj.current_player]:
            print("player in penalty box")
        #if self.in_penalty_box[self.current_player]:
            if player_obj.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                player_obj.purses[player_obj.current_player] += 1
                print(player_obj.players[player_obj.current_player] + \
                    ' now has ' + \
                    str(player_obj.purses[player_obj.current_player]) + \
                    ' Gold Coins.')

                winner = self._did_player_win()
                player_obj.current_player += 1
                if player_obj.current_player == len(player_obj.players): player_obj.current_player = 0

                return winner
            else:
                player_obj.current_player += 1
                if player_obj.current_player == len(player_obj.players): player_obj.current_player = 0
                return True

        else:
            # REFACTOR: needs spelling update (done)
            print("[NOT in penalty box]: Correct Answer!")
            # one gold coin added at index of current player
            player_obj.purses[player_obj.current_player] += 1
            print(player_obj.players[player_obj.current_player] + \
                ' now has ' + \
                str(player_obj.purses[player_obj.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            player_obj.current_player += 1
            # if last player is reached, then start over with first player
            if player_obj.current_player == len(player_obj.players): player_obj.current_player = 0

            return winner
    '''

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        # if last player is reached, then start over with first player
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


## Test Stuff ###
'''
    # test method
    def player_stuff(self): # note to self, self must always be there ...
        print("Player stuff method")
        x = player_obj.places
        return print(f"Places{x}")

    @property
    def _testprop(self):
        print("test prop")
        if player_obj.places[player_obj.current_player] == 0: return 'Pop'
        if player_obj.places[player_obj.current_player] == 4: return 'Pop'
        return 'Rock dude'
        # print("Player test prop")
        # x = player_obj.places
        # return print(f"Places test: {x}")
        '''