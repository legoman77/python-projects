age = input("What is your age?\n ")
age = age.strip()
age = int(age)

if age > 9000:
    print("THAT'S OVER 9000!!!!!!")
elif age == 1:
    print("You must be a very smart baby if you can use this program.")
elif age < 0:
    print("I'm pretty sure that's impossible...")

days = age * 365.242

print("You are {} years old or {} days old.".format(age,days))


