import random
from validation import validated_guess
from messages import display_message

length_combination = 4
max_tries = 10


def the_possible_values():
    values = [ str(number) for number in range(10) ]
    random.shuffle(values)
    return values[0:6]


def generate_new_combination(possible_values):
    return [ random.choice(possible_values) for possibilities in range(length_combination)]


if __name__ == "__main__":
    possible_values = the_possible_values()
    print("Generated possible values:", possible_values)

    assert len(possible_values) == 6
    assert len(set(possible_values)) == 6

    for value in possible_values:
        assert value in '0123456789', f"Unexpected value found: {value}"


def the_player_guess(player_try, right_combination):
    right_place = 0
    wrong_place = 0
    answer = right_combination.copy()
    guess = player_try.copy()

    for number in range(length_combination):
        if guess[number] == answer[number]:
            right_place += 1
            answer[number] = None
            guess[number] = None

    for value in guess:
        if value is not None and value in right_combination:
            wrong_place += 1
            right_combination[right_combination.index(value)] = None

    return right_place, wrong_place

