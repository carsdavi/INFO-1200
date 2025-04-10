#!/usr/bin/env python3

#import csv module needed to work with csv (comma-seperated) files

import csv

# create a global constant

FILE_NAME = "trips.csv"

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

# step 3: function that writes the data from a two-dimensional list named trips that's passed to it as an argument
def write_trips(trips):
    
# step 4: ata for each trip consists of miles driven, gallons of gas used, and the calculated MPG value

    with open(FILE_NAME, "w", newline="") as output_file: # open for write
        writer = csv.writer(output_file) # returns a CSV writer object
        writer.writerows(trips) # writes all specified rows of the trips list

# step 4: Add a read_trips() function that reads the data from the trips.csv file and returns the data for the trips in a two-dimensional list named trips.    
def read_trips():
    trips = [] # create list

    with open(FILE_NAME, "r", newline="") as input_file: #open file for reading
        reader = csv.reader(input_file)
        for row in reader: # process the rows in the reader object
            trips.append(row) # add each row to the trips list

    return trips # retun the address of the trips list

# step 4: Add a list_trips() function that reads the data from the trips.csv file and returns the data in the trips list on the console as shown above.

def list_trips(trips):

    # display headings

    print("Distance\tGallons\t\tMPG")

    # process each trip

    for trip in trips:
        print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")


    print()
    

def main():

    trips = [] # empty list
    
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    # step 4 call the read_trips() function and
    # assign the returned value to the trips variable

    trips = read_trips()

    # step 4: call the list_trips() function to display the contents trips

    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trip = [miles_driven, gallons_used, mpg]

        trips.append(trip)

        write_trips(trips)


        list_trips(trips)


        more = input("More entries? (y or n): ")


    
    print("Bye!")

if __name__ == "__main__":
    main()

