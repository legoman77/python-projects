
def die():
     print("Thou art cast into the Gorge of Eternal Peril.")
     print("You died.")
     
def live():
     print("Fine, off you go.")
     print("You live.")

def ask(question):
    answer = input(question)
    answer = answer.strip().lower()
    print("Thou hast answered {}".format(answer))
    return answer

def ask_color():
    answer = ask("What is your favorite color?\n ")
    return answer
            
    

    
    


#############################################

name = ask("What is your name?\n ")
quest = ask("What is your quest?\n ")


if name == 'lancelot':
    color = ask_color() 
    if color == 'blue':
        live()
    else:
        die()
elif name == 'robin':
    capital = input("What is the capital of Assyria?\n ")
    if capital == 'assur' or capital == 'ashur':
        live()
    else:
        die()
elif name == 'galahad':
    color = ask_color()
    if color == 'blue':
        die()
    else:
        live()
    
elif name == 'arthur':
    answer = input("What is the air speed velocity of an unladen swallow?\n ")
    if answer == 'what do you mean, an african or a european swallow?':
        live()
        print("The Bridgekeeper is thrown into the Gorge of Eternal Peril")
    elif answer == '25 mph':
        live()
    else:
        die()
else:
    color = ask_color()
    if color != '':
        live()
    else:
        die()
    







