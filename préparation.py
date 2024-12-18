import random

length_combination = 4
max_attempts = 10


def the_possible_values():
    values = [ str(number) for number in range(10) ]
    random.shuffle(values)
    return values[0,6]
