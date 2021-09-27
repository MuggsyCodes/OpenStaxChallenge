#request question data from API endpoint

# I used requests to make an API call to a quiz question generator app
# questions are returned as json data which I use as a dictionary in python 
import requests

parameters = {
    'amount': 48,
    'type': 'boolean'
}

#response = requests.get(url='https://opentdb.com/api.php', params=parameters)
#response.raise_for_status()
#question_data = response.json()['results']

raw = {"response_code":0,"results":[{"category":"Entertainment: Cartoon & Animations","type":"boolean","difficulty":"easy","question":"In the &quot;Shrek&quot; film franchise, Donkey is played by Eddie Murphy.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Film","type":"boolean","difficulty":"easy","question":"Han Solo&#039;s co-pilot and best friend, &quot;Chewbacca&quot;, is an Ewok.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"English new wave musician Gary Numan founded the video game development company Facepunch Studios in March 2009.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Geography","type":"boolean","difficulty":"easy","question":"The Republic of Malta is the smallest microstate worldwide.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Film","type":"boolean","difficulty":"easy","question":"Matt Damon played an astronaut stranded on an extraterrestrial planet in both of the movies Interstellar and The Martian.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Politics","type":"boolean","difficulty":"easy","question":"There was a satirical candidate named &quot;Deez Nuts&quot; running in the 2016 US presidential elections.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Film","type":"boolean","difficulty":"easy","question":"The 2010 film &quot;The Social Network&quot; is a biographical drama film about MySpace founder Tom Anderson.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"Big the Cat is a playable character in &quot;Sonic Generations&quot;.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"RAM stands for Random Access Memory.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"Ada Lovelace is often considered the first computer programmer.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Mythology","type":"boolean","difficulty":"easy","question":"According to Greek Mythology, Zeus can control lightning.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science & Nature","type":"boolean","difficulty":"easy","question":"An atom contains a nucleus.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Politics","type":"boolean","difficulty":"easy","question":"The 2016 United States Presidential Election is the first time Hillary Clinton has run for President.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"Deus Ex (2000) does not feature the World Trade Center because it was destroyed by terrorist attacks according to the game&#039;s plot.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"easy","question":"On average, at least 1 person is killed by a drunk driver in the United States every hour.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"The PlayStation was originally a joint project between Sega and Sony that was a Sega Genesis with a disc drive.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"The 2005 video game &quot;Call of Duty 2: Big Red One&quot; is not available on PC.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"In the &quot;Half-Life&quot; series, &quot;H.E.V&quot; stands for &quot;Hazardous Evasiveness Vest&quot;","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"The main playable character of the 2015 RPG &quot;Undertale&quot; is a monster.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"Danganronpa 2: Goodbye Despair featured all of the surviving students from the first game.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"In Splatoon, the Squid Sisters are named Tako and Yaki.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Geography","type":"boolean","difficulty":"easy","question":"St. Louis is the capital of the US State Missouri.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Board Games","type":"boolean","difficulty":"easy","question":"There is a Donald Trump Board Game, which was made in 1989.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"&quot;HTML&quot; stands for Hypertext Markup Language.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Japanese Anime & Manga","type":"boolean","difficulty":"easy","question":"In the &quot;Toaru Kagaku no Railgun&quot; anime,  espers can only reach a maximum of level 6 in their abilities.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"easy","question":"One of Donald Trump&#039;s 2016 Presidential Campaign promises was to build a border wall between the United States and Mexico.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"In Pok&eacute;mon Sun and Moon, a male Salandit can evolve to a Salazzle.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Animals","type":"boolean","difficulty":"easy","question":"A caterpillar has more muscles than humans do.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Politics","type":"boolean","difficulty":"easy","question":"One of Barack Obama&#039;s United States presidential campaign slogan&#039;s was &quot;Yes We Can&quot;.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Celebrities","type":"boolean","difficulty":"easy","question":"Marilyn Monroe was born on July 1, 1926.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"In &quot;Undertale&quot;, the main character of the game is Sans.","correct_answer":"False","incorrect_answers":["True"]},{"category":"History","type":"boolean","difficulty":"easy","question":"Adolf Hitler was tried at the Nuremberg trials.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"Linux was first created as an alternative to Windows XP.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Politics","type":"boolean","difficulty":"easy","question":"Donald Trump won the popular vote in the 2016 United States presidential election.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"In Heroes of the Storm, the Cursed Hollow map gimmick requires players to kill the undead to curse the enemy team.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Television","type":"boolean","difficulty":"easy","question":"In &quot;Star Trek&quot;, Klaang is a typical Klingon male.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Sports","type":"boolean","difficulty":"easy","question":"In Rugby League, performing a &quot;40-20&quot; is punished by a free kick for the opposing team.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Art","type":"boolean","difficulty":"easy","question":"Leonardo da Vinci was not the creator of the Mona Lisa.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Cartoon & Animations","type":"boolean","difficulty":"easy","question":"Waylon Smithers from &quot;The Simpsons&quot; was originally black when he first appeared in the series.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Video Games","type":"boolean","difficulty":"easy","question":"&quot;Metal Gear Solid 3: Snake Eater&quot; was released in 2004.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science: Mathematics","type":"boolean","difficulty":"easy","question":"The sum of any two odd integers is odd.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Japanese Anime & Manga","type":"boolean","difficulty":"easy","question":"In Chobits, Hideki found Chii in his apartment.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Politics","type":"boolean","difficulty":"easy","question":"Former president Theodore Roosevelt (1900-1908)  ran for another term under the Progressive Party in 1912.","correct_answer":"True","incorrect_answers":["False"]},{"category":"History","type":"boolean","difficulty":"easy","question":"The United States of America was the first country to launch a man into space.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Science: Mathematics","type":"boolean","difficulty":"easy","question":"An equilateral triangle always has every angle measuring 60&deg;.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"easy","question":"Vietnam&#039;s national flag is a red star in front of a yellow background.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Animals","type":"boolean","difficulty":"easy","question":"The internet browser Firefox is named after the Red Panda.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Sports","type":"boolean","difficulty":"easy","question":"There are a total of 20 races in Formula One 2016 season.","correct_answer":"False","incorrect_answers":["True"]}]}

# I will use this in my main function
question_list = raw['results'] # list of dictionaries


# print(question_list)

# I have a list of dictionaries
# I want to access the question from each dictionary
# I then want to move to the next item in the list
# def question_generator(question_list):
#     d1 = [dict["question"] for dict in question_list]
#     return d1

#print(question_generator(question_list))

# for i in range(0, len(question_list)-1, 3):
#     d1 = question_list[i]["question"]
#     print(d1)
#     d2 = question_list[i+1]["question"]
#     print(d2)
#     d3 = question_list[i+3]["question"]
#     print(d3)