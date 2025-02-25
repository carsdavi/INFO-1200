#Name: Carson Davis
#Class: INFO 1200
#Section: 001
#Professor: Jason Sharp
#Date: 02/25/2025
#Assignment #: Insert assignment number
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

# defining is_even function

def is_even(num):
    
    # decision structure to determine if there is a remainder

    if num % 2 == 0:
        return True # it's even
    else:
        return False # it's odd

# step 3 - define the main() function

def main():
    print("Carson's even or odd checker") # display message
    print() # display blank line

    # create variable and assign it a value from the user

    my_num = int(input("Enter an Integer: "))

    
    # function call passing the value of my_num as an argument
    if is_even(my_num):
        print ("This is an even number")
    else:
        print("This is an odd number")

if __name__ == "__main__": main()
