#!/usr/bin/env python3

# step 2 - display a welcome message
print("Carson Davis' Miles Per Gallon application")
print()


another_trip = "y" # step 2 - create variable and assign value

while another_trip == "y": # step 3 - condition to continue 

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon: ")) # step 3 - 

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
         print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0: # step 4 - input validation
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        total_gas_cost = round(gallons_used * cost_per_gallon, 1) # step 4
        cost_per_mile = round(total_gas_cost / miles_driven, 1) # step 4
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost) # step 4
        print("Cost Per Mile:             ", cost_per_mile) # step 4

    another_trip = input("Get entries for another trip (y/n)? ").lower()
        
print()
print("Bye")



