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
                    
                      
              
    
