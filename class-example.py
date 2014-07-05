# class example
attack = 20
defense = 30
health = 10
speed = 20


def print_stats(comment):
	print(comment)
	print("health: " + str(health))
	print("attack: " + str(attack))
	print("defense: " + str(defense))
 	

description = '''
you are in the room
'''
print(description)

answer = input("What will you do?\n>")

# print(answer)

while True:
	answer = input("What will you do?\n>")
	if answer == "":
		print("What was that?")
	elif answer == "drink potion":
		health *= 2
		print_stats("You feel much better")
	elif answer == "work out":
		attack += 2
		print_stats("You feel manly")
	elif answer == "put on armor":
		defense **= 2
		print_stats("You feel much safer")
		
