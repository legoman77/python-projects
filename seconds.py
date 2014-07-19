your_name = input("What is your name? ")

your_age = input("What is your age? ")
your_age = int(your_age)

your_seconds = your_age * 31536000

print("You are {} seconds old, {}.".format(your_seconds,your_name))
