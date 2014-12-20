import random

answers = ['Yes','No','Maybe']

while True:
    print('Welcome to the Magically Magic 8 Ball!')
    print('What is your question?')
    question = input('> ')
    answer = random.choice(answers)
    print(answer)
        
