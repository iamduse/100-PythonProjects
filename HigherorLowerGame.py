import random
import game_data
#TODO 1: Create a welcome message to the game
print("Play Compare Game")
#section A read the name and the description
#Pick random dictionary than use that dictionary to fetch the keys in the dictionaries
section_a = random.choice(game_data.data)
name = section_a["name"]
description =  section_a["description"]
follower_a = section_a["follower_count"]
print(f"COMPARE A: {name}, {description}")
print("\n"*1)
print("VS")
print("\n"*1)

section_b = random.choice(game_data.data)
name = section_b["name"]
description =  section_b["description"]
follower_b =  section_b["follower_count"]
print(f"COMPARE B: {name}, {description}")


# create a compare function
def compare(A,B):
    if follower_a > follower_b:
        return "a win"
    else:
        return "B win"


should_continue = True
while should_continue:
    choice = input("Who has more followers type 'a' or 'b': ")
    if choice:
        result = compare(section_a, section_b)
        print(result)
        break





