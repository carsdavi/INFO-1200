
#Name: Carson Davis
#Class: INFO 1200
#Section: MO4 Project
#Professor: Sharp
#Date: 02/17/2025
#Assignment #: 4
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.


print("Carson Davis' Letter Grade Converter") # step 2 - Showcase title
print()

choice="y" # create variable to be y
while choice.lower() =="y": # to take y or Y 
    number = int(input("Enter numerical grade:  ")) # initial integer input for outcome


# number rules for if
    if number >= 94:
        letter = "A"
    elif number >= 90:
        letter = "A-"
    elif number >= 87:
        letter = "B+"
    elif number >= 84:
        letter = "B"
    elif number >= 80:
        letter = "B-"
    elif number >= 77:
        letter = "C+"
    elif number >= 74:
        letter = "C"
    elif number >= 70:
        letter = "C-"
    elif number >= 67:
        letter = "D+"
    elif number >= 64:
        letter = "D"
    elif number >= 60:
        letter = "D-"
    else:
        letter = "E" # rule for everything else to E

    print(f"Letter grade: {letter}") #display letter grade
    print()
    choice = input("Continue? y/n: ") #display question
    print()


print("Bye!") #display goodbye message
