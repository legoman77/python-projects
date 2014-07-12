your_name = input("What's yo name bro?\n ").strip().title()
print("Yo yo " +  your_name + "!")

other_name = input("What's yo bro's name?\n ").strip().title()
print("Yo yo " + other_name + "!")

your_age = input("What's yo age?\n ")
your_age = int(your_age)

other_age = input("What's yo bro's age?\n ")
other_age = int(other_age)

years_apart = (your_age - other_age)
years_apart = abs(years_apart)

days_apart = years_apart * 365.242

print("You are {} years apart or {} days apart".format(years_apart,days_apart))


