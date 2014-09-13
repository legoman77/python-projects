import random

love = random.randrange(1,100)

print("Welcome to the Lovinator!")
print("Please enter Person 1's name.")
name1 = input("> ")

print("Please enter Person 2's name.")
name2 = input("> ")

print("{} and {}'s love rating is {}%".format(name1,name2,love))
