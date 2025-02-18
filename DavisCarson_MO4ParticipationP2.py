#!/usr/bin/env python3

# display a welcome message
print("Welcome to Carson Davis' Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # step 8 - create variable is_valid, assign false

    is_valid = False

    # step 8 - create while loop for is_valid

    while is_valid == False:

        #get input from user
        monthly_investment = float(input("Enter monthly investment:\t"))

        # stpe 8 - if statement to validate range

        if monthly_investment > 0 and monthly_investment <= 1000:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 1000. Please Try Again.")

    is_valid = False # step 8 - set is valid back to false

    # step 9 -  create while loop for validation
    
    while is_valid == False:

        
        # get input from the user
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        is_valid = True

        
        if yearly_interest_rate > 0 and yearly_interest_rate <=15:
            is_valid = True # step 9 is valid to true
        else:
            # step9 - display error message
            print("Entry must be greater than 0 and less than or equal to 15. Please Try Again.")

        is_valid = False # step 9 - set variable back to false


        # step 10 - range of values
        years = int(input("Enter number of years:\t\t"))

        if years > 0 and years <= 50:
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than or equal to 50. Please Try Again.")
        is_valid = False 


       

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()
    

print("Bye!")
