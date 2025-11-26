import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#option one we will use random.choose module
print(random.choice(friends))

#option two we will use randomInt using the amount of the list as an range
choose_index = random.randint(a=0,b=4)
print("the unlucky mate this time is: ")
print(friends[choose_index])


