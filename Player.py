# Create player class

import random

# players_available = ["Mike", "Dennis", "Marvin", "Neil", "Chris", "Otto", "Phil" ]

# creating Player class using same variable names for ease 
class Player:
    def __init__(self):
        # I might have to change this init list structure
        self.players = [] ## Player class ##
        self.places = [0] * 6 # corresponds to location # list of length 6 - why? 
        self.purses = [0] * 6 # this is the gold coins score
        self.in_penalty_box = [0] * 6 # stores 0 or boolean T/F values 

        # start game with first player in list (index 0)
        self.current_player = 0 ## Player class ##
        self.is_getting_out_of_penalty_box = False
    

    def add(self, player_name):
        self.players.append(player_name)

        # *** this appears to be redundant because it replaces 0 with 0 *** #
        #self.places[self.how_many_players] = 0 # what exactly is going on here? # not understanding how_many_players property
        
        # *** this appears to be redundant because it replaces 0 with 0 *** #
        #self.purses[self.how_many_players] = 0
        # players start off NOT inside the penalty box 
        # Is this even needed if all values start at 0?
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def is_playable(self):
        return self.how_many_players >= 2


player = Player()
player.add_player(random.choice(players_available))
print(player.player_length) 

# class Player:
#     # initialize Player class
#     def __init__(self):
#         self.player_list = []
#         # first name/player in the list will begin play
#         self.current_player = 0


#     @property
#     def player_length(self):
#         return len(self.player_list)

#     # add player method
#     def add_player(self, player_name):
#         self.player_list.append(player_name)
#         print("%s was added as a player" % player_name)
#         print( "%s is player number %s" % (player_name, len(self.player_list)) )




