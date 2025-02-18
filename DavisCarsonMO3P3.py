#!/usr/bin/env python3
print("Carson Davis Rectangle App") # display app name

# display a welcome message
print("The area and perimeter program")
print()

# get input from the user
length = float(input("Please enter the length:\t\t"))
width = float(input("Please enter the width:\t"))

# calculate miles per gallon
area = length * width

#calculate perimeter
perimeter = 2 * length + 2  * width

            
# format and display the result
print()
print("Area = " + str(area))
print("Perimeter = " + str(perimeter))
print()
print("Thanks for using this program!")


