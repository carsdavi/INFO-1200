#Name: Carson davis
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: 04/3/2025
#Assignment #: 8
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

# step 1: create display title function
def display_title():
    print("Carson Davis' Wizard Inventory Game")
    print()

# step 1: create display menu function
def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

#step 3: create show function

def show(inventory):
    # create a for loop that loops through all items that are held by the wizard
    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item}")
    print() # display blank line

# step 3: Create a grab_item() function that receives the inventory as a parameter

def grab_item(inventory):
    #If the number of items is more than or equal to 4
    if len(inventory) >= 4:
        #display the text "You can't carry any more items. Drop something first"
        print("You can't carry any more items. Drop something first.\n")
    else: # Otherwise
        item = input("Name: ")
        inventory.append(item)
        print(f"{item} was added.\n")

# step 2 create main function

def main():
    display_title() # step 2: call display title function
    display_menu() # step 2: call display menu function

    inventory = ["staff", "boulder", "hat"] # step 2: create a list

    #Create a while loop that executes until the user types exit
    while True:        
        command = input("Command: ")  # store the user's input in a variable called "command"
        # create an if, elif, elif,... for each of the command menu items        
        if command == "show":
            show(inventory)
        elif command == "grab":
            grab_item(inventory)
        elif command == "edit":
            edit_item(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
            




# if started as the main module, call the main function
if __name__ == "__main__":
    main()

    
Create a new Python file, saving the file with this naming format LastNameFirstName_FinalQ2.py, that includes 5 of the 8 items listed:

YOU MUST HAVE A LINE OF PSEUDOCODE FOR ALL LINES OF SOURCE CODE

The program MUST be uniquely created during the final exam time. A previously created or submitted program, participation, or project may NOT be submitted and will NOT be accepted for credit. A separate question follows for uploading the created Python (.py) file.

Items:

 Input validated as a float number (Must not break if "Ten" is an input).
 Display a value rounded to 3 decimal places
 Create an if-elif-else statement
 Read a .csv or .txt file
 Write to a .csv or .txt file
 For loop and print all items inside the loop
 List that holds a two-dimensional list
 GUI with at least one control
Describe each option you chose to implement in the text box provided.
