class Hero(): pass

class Creature():pass

spheal = Hero()

noobsimba = Creature()



spheal.health = 20
spheal.attack = 5
spheal.defense = 2
spheal.speed = 1
spheal.cuteness = 10

noobsimba.health = 10
noobsimba.attack = 5
noobsimba.defense = 1
noobsimba.speed = 3

##################################

print("A Noob Simba appears!")

while True:
    if noobsimba.speed > spheal.speed:
        sphealdamage = noobsimba.attack - spheal.defense
        spheal.health = spheal.health - sphealdamage
        print("The Noob Simba attacks!")
        print("Spheal took {} damage!".format(sphealdamage))
        print("Spheal has {} HP remaining.".format(spheal.health))
        if spheal.health > 0:
            print("What will Spheal do?")
            print("Attack")
            print("Special")
            print("Items")
            sphealmove = input("> ")
            if sphealmove == 'attack':
                print("Spheal attacks!")
                noobsimbadamage = spheal.attack - noobsimba.defense
                noobsimba.health = noobsimba.health - noobsimbadamage
                print("The Noob Simba took {} damage!".format(noobsimbadamage))
            if sphealmove == 'special':
                print("Which move should Spheal use?")
                print("Rollout")
                print("Mamo")
                print("Blizzard")
                sphealspecial = input("> ")
                if sphealspecial == 'rollout'

    if noobsimba.health <= 0:
        print("The Noob Simba was defeated!")
        print("You won the battle!")
        break
    if spheal.health <= 0:
        print("Spheal was deafeated...")
        print("You lost the battle...")
        break              
              
    
