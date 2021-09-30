
# testing wrapper functions
from random import randrange

roll = randrange(0,6)

# the key should be found in a list of possible ints 
# How do I do this? 
# How do I generate a random category
# Depending on the randint, look inside a list - can a list be a key? 
# Key can be a tuple!

def random_category(category_string):
    

def switcher(argument):
    category_switcher = {
        0: 'Pop',
        4: 'Pop',
        8: 'Pop',
        1: 'Science',
        5: 'Science',
        9: 'Science',
        2: 'Sports',
        6: 'Sports',
        10: 'Sports',
    }
    # get value from dictionary based on argument 
    category = category_switcher.get(argument, 'Rock')
    #print(f"Chosen category: {category}")
    return category

def test_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@test_decorator
def test_string():
    print("Howdy!")

# call function that is decorated - WORKING
#test_string()

def math_decorator(func):
    def inner(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return inner

@math_decorator
def math_fun(num_list):
    c = 0
    for number in num_list:
        c+=number
    # return sum of all numbers in list
    return print(f"math fun result: {c}")

math_fun([1,2,3])

