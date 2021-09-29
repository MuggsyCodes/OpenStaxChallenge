
# testing wrapper functions


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

