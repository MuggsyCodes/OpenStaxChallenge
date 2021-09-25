class Questions:

    def __init__(self):

        self.pop_questions = [] #* Question Class *#
        self.science_questions = [] 
        self.sports_questions = []
        self.rock_questions = []

        # game is initiated with 50 dummy questions in each category
        # this could also be done talking to a site via an API
        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    # why was this done separately? 
    # this could be done for all questions
    def create_rock_question(self, index):
        return "Rock Question %s" % index