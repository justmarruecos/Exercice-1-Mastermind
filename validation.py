def validated_guess(player_try, possible_values):
    guess_list = player_try.split()
    if len(guess_list) != 4:
        raise ValueError("Your try must contain 4 values.")
    if any(value not in possible_values for value in guess_list):
        raise ValueError(f"All values must be in {', '.join(possible_values)}.")
    return guess_list
