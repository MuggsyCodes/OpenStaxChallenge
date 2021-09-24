# Create player class

import random

players_available = ["Mike", "Dennis", "Marvin", "Neil", "Chris", "Otto", "Phil" ]

class Player:
    # initialize Player class
    def __init__(self):
        self.player_list = []
        # first name/player in the list will begin play
        self.current_player = 0


    @property
    def player_length(self):
        return len(self.player_list)

    # add player method
    def add_player(self, player_name):
        self.player_list.append(player_name)
        print("%s was added as a player" % player_name)
        print( "%s is player number %s" % (player_name, len(self.player_list)) )


a_list = [0] * 6

print(a_list)
for item in a_list:
   print(item)

player = Player()
player.add_player(random.choice(players_available))
print(player.player_length)



