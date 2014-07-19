print("Welcome to the Pixelmon Quiz!")

answer1 = input("Question 1: What is the only Pixelmon that cannot be obtained without commmands?\n ")
answer1 = answer1.lower()
answer1 = answer1.strip()

if answer1 == "porygon":
    print("Correct!")
else:
    print("Incorrect...") 
     
answer2 = input("Question 2: How many species of Pixelmon may drop vines when defeated?\n ")
answer2 = answer2.lower()
answer2 = answer2.strip()

if answer2 == "ten":
    print("Correct!")
elif answer2 == "10":
    print("Correct!")
else:
    print("Incorrect...")

answer3 = input("Question 3: What is one of the two items wild Sableye may drop when defeated?\n")
answer3 = answer3.lower()
answer3 = answer3.strip()

if answer3 == "diamonds":
    print("Correct!")
elif answer3 == "ghast tears":
    print("Correct!")
else:
    print("Incorrect...")
