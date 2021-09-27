# this is to keep track of score inside data file
import pandas as pd

# test data
player_list = ["dan", "ace", "tom"]
player_score = [1, 2, 3]
#test_dictionary = {"one": 1, "two":2, "three":3,}

class Score:
    '''report current score and create data file of player scores'''
    def report_score(self, player_list, player_score):
        # create a dictionary from the inputs
        d = dict(zip(player_list, player_score))
        self.score = d
        # print each name: score
        for item in d:
            print(f"{item} current score: {d[item]}")
        # use dictionary item to create dataframe
        df = pd.DataFrame(d, index=["a","b","c"])
        print(df)
        # return score dataframe
        return df


    def score_file(self, dataframe):
        # create a dataframe from a dictionary
        # update CSV file from dictionary 
        # Depending on who wins, let's update the file to reflect total wins
        # could also make this time stamped so we have a record of games 
        dataframe.to_csv("game_data.csv", index=False)
        print("score file created")


# testing Score 
s = Score()
my_file = s.report_score(player_list, player_score)
s.score_file(my_file)
