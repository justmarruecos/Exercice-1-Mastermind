import random

length_combination = 4
max_tries = 10


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


def the_player_guess(try, right_combination):
    right_place = 0
    wrong_place = 0
    answer = right_combination.copy()

    for number in range(length_combination):
        if try[number] == answer[number]:
            right_place += 1
            answer[number] = None
            try[number] = None

    for value in try:
        if value is not None and value in right_combination:
            wrong_place += 1
            right_combination[right_combination.index(value)] = None

    return right_place, wrong_place



def play_game():
    possible_values = the_possible_values()
    right_combination = generate_new_combination(possible_values)
    attempts_left = max_tries

    display_message(f"Possible values: {', '.join(possible_values)}")
    display_message(f"Try to guess the {length_combination}-digit combination in {max_tries} attempts!")

    for attempt in range(max_tries):
        guess = validate_guess(input("Enter your guess: "), possible_values)
        well_placed, misplaced = the_player_guess(guess, right_combination)

        display_message(f"Well-placed: {well_placed}, Misplaced: {misplaced}")

        if well_placed == length_combination:
            display_message("🎉 Congratulations! You guessed the combination!")
            break
    else:
        display_message(f"😭 Game Over! The right combination was: {''.join(right_combination)}")
