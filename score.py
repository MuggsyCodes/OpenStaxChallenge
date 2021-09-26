# this is to keep track of score inside data file

player_list = ["one", "two", "three"]
player_score = [1, 2, 3]

class Score:
    '''report current score and create data file of player scores'''
    def report_score(self, player_list, player_score):
        # create a dictionary from the inputs
        d = dict(zip(player_list, player_score))
        self.score = d
        print(self.score)
        # return score dictionary
        return self.score


    def score_file(self, dictionary):
        # create a dataframe from a dictionary
        # update CSV file from dictionary 
        # Depending on who wins, let's update the file to reflect total wins
        # could also make this time stamped so we have a record of games 
        pass