
from player import Player


# Roll class

class Roll:

    # NOTE: probably need to rename the argument something different than the method for clarity
    def roll(self, roll_value):
        print("%s is the current player" % self.players[self.current_player])
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
                print("The category is %s" % self._current_category)
                self._ask_question()
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
            print("The category is %s" % self._current_category)
            self._ask_question()
