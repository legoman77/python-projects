def ask(question):
    answer = input(question)
    answer = answer.strip().lower()
    print("You answered: {}".format(answer))
    return answer

def likes(food):
    yeah = ('yeah','yes','yup','uhun')
    answer = ask('Do you like {}?'.format(food))
    return answer.startswith(yeah)

def doo_doo_doo_dupe():
    print('''
Doo, doo doo dupe, can't wait to get a mouthful!
''')


#------------------------------------------------------------

if likes('waffles'):
    if likes('pancakes'):
        if likes('french toast'):
                 doo_doo_doo_dupe()
