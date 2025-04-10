#!/usr/bin/env python3

# import csv module needed to work with csv (comma-seperated) files

import csv

# create a global constant for the file name
FILE_NAME = "trips.csv"

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # step 2: create a two-dimensional list (list of lists) for each trip

    trips = [] # empty list
    
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        # step 2: place the input values into the trip list

        trip = [miles_driven, gallons_used, mpg]

        # step 2: add the trip list to the trips list of lists

        trips.append(trip)
        
        more = input("More entries? (y or n): ")

        # step 2: save the data in the trips list to a file named trips.csv

        with open(FILE_NAME, "w", newline="") as output_file: # open for write
            writer = csv.writer(output_file) # returns a CSV writer object
            writer.writerows(trips) # writes all specified rows of the trips list
    
    print("Bye!")

if __name__ == "__main__":
    main()

