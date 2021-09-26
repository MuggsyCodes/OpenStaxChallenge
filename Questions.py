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


    # I need to use HTML unescape to make the question look better
    def question_bank(self, question_list):
        for i in range(0, len(question_list)-1, 4):
            self.pop_questions.append("Pop Question: %s" % question_list[i]["question"])
            self.science_questions.append("Science Question: %s" % question_list[i+1]["question"])
            self.sports_questions.append("Sports Question: %s" % question_list[i+2]["question"])
            self.rock_questions.append("Rock Question: %s" % question_list[i+3]["question"])
                
    def dummy(self):
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
        #print(f"Chosen category: {category}")
        return category

    # define functions when categories are chosen
    def pop(self):
        return print(self.pop_questions.pop(0))
    
    def science(self):
        return print(self.science_questions.pop(0))

    def sports(self):
        return print(self.sports_questions.pop(0))

    def rock(self):
        return print(self.rock_questions.pop(0))


    def big_switcher(self, argument):
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
        print(f"Chosen Kategory: {category}")
        #return category

        # nested function inside big_switcher
        def _ask_question(self, category):
            ### begin switch dict code 
            print("This is to be used inside inner1 function")
            question_dictionary = {
                'Pop': self.pop,
                'Science': self.science,
                'Sports': self.sports,
                'Rock': self.rock,

            }
            my_func = question_dictionary.get(category, lambda: "Undefined Category")
            my_func()
        return _ask_question(self, category)

    # Use this to combine category selector and ask question
    # I couldn't quite get this to work
    def category_decorator(func):
        def inner1(self, argument):
            print("Inner function inside category decorator was called.")
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
            print(f"Chosen Kategory (reached inner1): {category}")
            func(self, category)
            print("After function was executed.")
            return category

        return inner1

    # Questions class #
    # Definitey can use switch statement here
    # Why? Because all if statements have to be evaluated each time which is inefficient
    # --- this almost works but prints all questions after only single category chosen ---- #
    @category_decorator
    def _ask_question(self, category):
        ### begin switch dict code 
        print("This is to be used inside inner1 function")
        question_dictionary = {
        'Pop': self.pop,
        'Science': self.science,
        'Sports': self.sports,
        'Rock': self.rock,

    }
        my_result = question_dictionary.get(category, lambda: "Undefined Category")
        print(my_result)
        return my_result


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


    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        # if last player is reached, then start over with first player
        if self.current_player == len(self.players): self.current_player = 0
        return True


    ### Test stuff ### 

    #return _ask_question
    # def _ask_question(self, quest_catgy):
    #     ### begin switch dict code 
    #     print("This is to be used inside inner1 function")
    #     question_dictionary = {
    #         'Pop': print(self.pop_questions.pop(0)),
    #         'Science': print(self.science_questions.pop(0)),
    #         'Sports': print(self.sports_questions.pop(0)),
    #         'Rock': print(self.rock_questions.pop(0)),

    #     }
    #     qc = question_dictionary.get(quest_catgy, "Undefined Category")
    #     print(f"Inside ask_question: {qc}")

        # if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        # if self._current_category == 'Science': print(self.science_questions.pop(0))
        # if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        # if self._current_category == 'Rock': print(self.rock_questions.pop(0))


    '''
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
        return "Rock"
    '''

    
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