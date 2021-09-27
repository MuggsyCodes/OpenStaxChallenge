# Create player class

import time

available_players = ["Neil", "Phil", "Chris", "Otto", "Marvin", "Dennis", "Mike"]

class Player:
    def __init__(self):
        # I might have to change this init list structure
        self.players = [] ## Player class ##
        # I changed all these lists to be added to upon new player creation
        # Why? So that the number of players is not limited
        self.places = [] #[0] * 6 #6 # corresponds to location # list of length 6 - why? 
        self.purses = [] #[0] * 6 # this is the gold coins score
        self.in_penalty_box = [] # Let's try an empty list here [0] * 6 # stores 0 or boolean T/F values
        # test value
        #self.test_player = "Carlos"

        # start game with first player in list (index 0)
        self.current_player = 0 ## Player class ##
        self.is_getting_out_of_penalty_box = False


    def roll(self, roll_value, questions_obj):
        print("%s is the current player and is ready to roll..." % self.players[self.current_player])
        #pause the output of the roll to make game play smoother
        time.sleep(.25)
        print("They have rolled a %s" % roll_value)
        # if TRUE - NOT 0 or False, this evaluates
        # # note: any number true EXCEPT 0
        if self.in_penalty_box[self.current_player]:
            if roll_value % 2 != 0: # look for ODD number
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = self.places[self.current_player] + roll_value
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(self.players[self.current_player] + \
                            '\'s new location is ' + \
                            str(self.places[self.current_player]))
                #print("The SWITCHER category is %s" % questions_obj.switcher(self.places[self.current_player]))            
                #print("The category is %s" % self._current_category)
                # test var #
                questions_obj.big_switcher(self.places[self.current_player])
                # end test var #
                # questions_obj._ask_question(self.places[self.current_player]) -- doesn't quite work
                #self._ask_question()
            else: # if player rolls an EVEN number 
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else: # if player NOT in penalty box
            # update current player location
            self.places[self.current_player] = self.places[self.current_player] + roll_value
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12
            # I think this needs and else statement here or is the if statement dithers 
            print(self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player]))
            #print("The SWITCHER category is %s" % questions_obj.switcher(self.places[self.current_player]))
            # *** call test function for switching map *** #
            questions_obj.big_switcher(self.places[self.current_player])
            #print("The category is %s" % self._current_category)
            # test var #
            #category_var = questions_obj.switcher(self.places[self.current_player])
            # end test var #
            # questions_obj._ask_question(self.places[self.current_player]) -- doesn't quite work
            #self._ask_question()
    

    def add(self, player_name):
        # add player name to players list
        self.players.append(player_name)
        #print(f"players list within Player Class: {self.players}")

        # *** this appears to be redundant because it replaces 0 with 0 *** #
        #self.places[self.how_many_players] = 0 # what exactly is going on here? # not understanding how_many_players property
        
        # *** this appears to be redundant because it replaces 0 with 0 *** #
        #self.purses[self.how_many_players] = 0
        # players start off NOT inside the penalty box 
        # Is this even needed if all values start at 0?
        #self.in_penalty_box[self.how_many_players] = False
        self.in_penalty_box.append(False)
        # add 0 to the places list when adding a new player
        self.places.append(0)
        self.purses.append(0)
        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    # must have at least 2 players for the game to run 
    def is_playable(self):
        return self.how_many_players >= 2

    def _did_player_win(self):
        print(f"{self.players[self.current_player]} Wins the Game!")
        return not (self.purses[self.current_player] == 6)




