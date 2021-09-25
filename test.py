# Using this script as a test bed for my changes
# Import classes from other files

from questions import Questions
from player import Player
#from roll import Roll

#instantiate new Player object
player = Player()
test_player = player.test_player
print(f"Test player: {test_player}")

timmy = player.add("Timmy")
print(timmy)

# instaniate new Question object
question = Questions()
test_question = question.test_question
print(f"Test question: {test_question}")

question.player_stuff()
# AttributeError: 'Questions' object has no attribute 'places'

question._testprop

#player.roll(4)
# works until: AttributeError: 'Player' object has no attribute '_current_category'
# _current_category attribute is part of question class 
'''What needs to happen exactly? 
* question needs to have reference to newly created player object
'''