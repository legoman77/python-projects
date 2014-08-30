import random

answers = [

    "Signs point to yes. ",
    "Yes. ",
    "Reply hazy, try again. ",
    "Without a doubt. ",
    "My sources say no. ",
    "As I see it, yes. ",
    "You may rely on it. ",
    "Concentrate and ask again. ",
    "Outlook not so good. ",
    "It is decidedly so. ",
    "Better not tell you now. ",
    "Very doubtful. ",
    "Yes - definitely. ",
    "It is certain. ",
    "Cannot predict now. ",
    "Most likely. ",
    "Ask again later. ",
    "My reply is no. ",
    "Outlook good. ",
    "Don't count on it. ",

]

while True:
    print("Ask me a question.")
    question = input('> ')
    if 'mudkipz' in question:
        print("i liek mudkipz")
        answers.append("i liek mudkipz")




    answer = random.choice(answers)
    print(answer)
