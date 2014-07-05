your_name = input("What's yo name bro?\n ")
print("Yo yo " +  your_name + "!")

other_name = input("What's yo bro's name?\n ")
print("Yo yo " + other_name + "!")

your_age = input("What's yo age?\n ")
your_age = int(your_age)

other_age = input("What's yo bro's age?\n ")
other_age = int(other_age)

years_apart = (your_age - other_age)
years_apart = abs(years_apart)

print("You are " + str(years_apart) + " years apart ")


