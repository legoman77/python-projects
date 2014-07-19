print("Hello World!")

name = input("What is your name?\n ")
name = name.strip()
name = name.title()

age = input ("What is your age?\n ")
age = int(age)
age = age.strip()

color = input ("What is your favorite color?\n ")
color = color.strip()

print("Hello {} who is {} years old and likes the color {}. ".format(name,age,color))
