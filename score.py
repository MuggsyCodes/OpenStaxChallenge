# this is to keep track of score inside data file
from os import name
import pandas as pd
from datetime import datetime

# test data
player_list = ["dan", "ace", "tom"]
player_score = [1, 3, 7, 0, 0, 0]
#test_dictionary = {"one": 1, "two":2, "three":3,}

class Score:
    '''report current score and create data file of player scores
    player score and player list are both lists of score and name, respectively.'''
    def report_score(self, player_list, player_score):
        # player score array has to match size of player list
        # iterate through player score for number of players
        # y = len(player_list)
        # for i in range(0, y):
        #     z = player_score[i]
        #     print(z)
        x = [player_score[i] for i in range(0, len(player_list))]
        # create a dictionary from the NEW SCORE list which is now right-sized
        d = {"Name": player_list, "Score": x}
        #d = dict(zip(player_list, player_score))
        #self.score = d
        # print each name: score
        name_score = [(key, value) for key, values in d.items() for value in values]
        print(name_score)
        # Winning ugly to try to get the names and gold coins score to show up
        # starting with a dictionary of list ints
        A = []
        B = []
        for my_tuple in name_score:
            if 'Name' in my_tuple:
                x = my_tuple[1]
                A.append(x)
                #print(x)
            else:
                y = my_tuple[1]
                B.append(y)
                #print(y)
        #print(A, B)
        c=0
        for a_item in A:
            print(f"Player {a_item}, has {B[c]} Coins")
            c+=1
         # Index not required
        df = pd.DataFrame(d)#, index=[f"Final Score: {c_t}"])
        #print(df)
        # return score score dictionary
        return d


    def score_file(self, a_dict):
        # if not not_a_winner: 
        # open existing score file --> create dataframe from CSV --> 
        # append new final score to DATAFRAME --> rewrite CSV file
        # add time stamp to dictionary
        # get time to create datestamp
        current_time = datetime.now()
        # dd/mm/YY H:M:S
        c_t = current_time.strftime("%d/%m/%Y") #%H:%M:%S")
        #print("date and time =", c_t)
        #a_dict["Time stamp"] = c_t
        # use dictionary item to create dataframe
        # include final score timestamp for records
        try:
            # open existing CSV file with scores
            df_score = pd.read_csv("game_data.csv")
        except FileNotFoundError as e:
            print(e)
            # create dataframe 
            indy = a_dict["Name"]
            df = pd.DataFrame(a_dict)#, index=indy)
            df.to_csv("game_data.csv", index=False)
            print("New File Created")
            # with open("game_data.csv", 'w') as file_obj:
            #     dummy_dictionary = {"one": 1, "two":2, "three":3, "four":4,}
            #     dummy_df = pd.DataFrame(dummy_dictionary, index=[0])
            #     dummy_df.to_csv("game_data.csv", index=True)
        else:
            # data frame from existing text file        
            print(f"DataFrame from opening csv\n{df_score}")
            # get list of scores from dictionary arg
            s_l = a_dict["Score"]
            n_l = a_dict["Name"]
            #print(s_l, n_l)
            df_2 = pd.DataFrame(a_dict)
            # assign new values to data_from read from CSV
            score_title = "score"+c_t
            #df_2 = df_score.assign(name = n_l, score_title = s_l)
            #print("Updated score")
            #print(f"DataFrame from dictionary argument\n{df_2}")
            # append new dataframe to NEXT COL of df_score dataframe
            df_new = pd.concat([df_score, df_2], axis=1)
            #print(f"DataFrame from COMBINED DFs\n{df_new}")
            #df_score = df_score.append(a_dict, ignore_index=True)
            #df_score.loc[len(df_score.index)] = a_dict
            # df_updated = df_score.append(data_frame)
            #print(df_score)
            df_new.to_csv("game_data.csv", index=False)
            print("Score file UPDATED")
            # Depending on who wins, let's update the file to reflect total wins



# testing Score 
#s = Score()
#d = s.report_score(player_list, player_score)
#s.score_file(d)