import random

top_of_range = input("Enter the top of the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    