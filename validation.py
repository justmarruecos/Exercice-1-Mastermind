def validated_guess(player_try, possible_values):
    guess_list = player_try.split()
    if len(guess_list) != 4:
        raise ValueError("Your try must contain 4 values.")
    if any(value not in possible_values for value in guess_list):
        raise ValueError(f"All values must be in {', '.join(possible_values)}.")
    return guess_list

#pour accepter les autres formes sans espace et avec virgule 
""" 

    guess = guess.replace(",", " ")
    if len(guess.strip()) == length_combination and guess.isdigit():
        guess_list = list(guess)
    else:
        guess_list = guess.split()

    if len(guess_list) != length_combination:
        raise ValueError(f"Your guess must contain exactly {length_combination} values.")
    if any(value not in possible_values for value in guess_list):
        raise ValueError(f"All values must be in {', '.join(possible_values)}.")

    return guess_list
 """