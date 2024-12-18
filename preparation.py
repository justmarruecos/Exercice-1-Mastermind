import random

length_combination = 4
max_attempts = 10


def the_possible_values():
    values = [ str(number) for number in range(10) ]
    random.shuffle(values)
    return values[0:6]


def generate_new_combination(the_possible_values):
    return [ random.choice(the_possible_values) for possibilities in range(length_combination)]


if __name__ == "__main__":
    possible_values = the_possible_values()
    print("Generated possible values:", possible_values)

    assert len(possible_values) == 6
    assert len(set(possible_values)) == 6

    for value in possible_values:
        assert value in '0123456789', f"Unexpected value found: {value}"