# Write your code here
import random

name = input("Enter your name:")
print("Hello, " + name )
user_score = 0

#update score if one already exists
ratings = open("rating.txt")
for line in ratings.readlines():
    if name.lower() in line.lower():
        user_score = int(line.split()[1])
        break
ratings.close()

options = input().split(",")
if len(options) < 2:
    options = ["rock", "paper", "scissors"]

rules = {}

#key = item, values = list of choices that beat item
for item in options:
    i = options.index(item)
    new_list = options[i+1:] + options[:i]
    rules[item] = [item for item in new_list[:len(new_list) // 2]]

print("Okay, let's start")

while True:
    user_choice = input()
    if user_choice == "!exit":
        print("Bye!")
        break
    if user_choice == "!rating":
        print("Your rating: " + str(user_score))
    elif user_choice in options:
        computer_choice = random.choice(options)
        if user_choice == computer_choice:
            user_score += 50
            print("There is a draw. ({})".format(computer_choice))
        elif computer_choice in rules[user_choice]:
            print("Sorry, but computer chose {}".format(computer_choice))
        elif user_choice in rules[computer_choice]:
            user_score += 100
            print("Well done. Computer chose {} and failed".format(computer_choice))
    else:
        print("Invalid input")