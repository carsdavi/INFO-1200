'''
Output: First Name, Last Name, Total Price
Input: First Name, Last Name, Total Price
Process: Multiply Number of Malasadas Purchased by Price of each Malasada

'''

#!/usr/bin/env python3

#Name: Carson Davis
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: 1/28/2025
#Assignment #: 3
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

#version 0.0

print("Lillith's 'Mazing Malasadas") #display company sign  

print("\"Home of the 'Mazing Malasadas!\"") #display slogan with double quotations

print() #display blank line

firstName = input ("Enter first name:") # prompt & assign the value to the variable
#first_name = "Joe" # assign the value to the variable
lastName = input("Enter last name:") # prompt & assign value to the variable
malasadasPurchased = int(input("Enter number purchased: ")) # assign value to the variable
malasadasPrice = float(input("Enter price: ")) # assign value to the variable

totalcost = malasadasPurchased * malasadasPrice #calculate total cost

print(firstName) # display first name
print(lastName) # display last name
print(round(totalcost)) # display total cost

print ("Total cost is $", round(totalcost,2)) #display total cost with comma

print(firstName + " " + "\n" + lastName +"\n") # concatenate first and last name

print("The total cost of the order is: " + str(round(totalcost))) # display total cost
