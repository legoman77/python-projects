import random

answers = ["Yes","No","Maybe"]


print("I am the 8 ball, hear my wisdom.")

while True:
    question = input("Ask me a question.\n")
    answer = random.choice(answers)
    print(answer)
