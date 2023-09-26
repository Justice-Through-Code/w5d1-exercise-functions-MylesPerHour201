# tip_calculator.py
# AS A GROUP, POD 1, WE COLLECTIVELY WORKED ON THIS ASSIGNMENT UNTIL 9:15PM 9/25/23 AND PASSED UNITTEST

# TODO: Create a function named calculate_tip
try:  #DO NOT MODIFY
        def tip_calculator():
            total_cost = float(input('The cost of the meal (without tax)'))
            num_people = int(input('The number of people splitting the bill'))
            tip_percentage = float(input('The tip percentage'))
            sales_tax = total_cost * .10
            tip = (total_cost * tip_percentage) / 100
            total_bill = float(total_cost + sales_tax + tip)
            bill_per_person = float(total_bill / num_people)

            print(f'Total bill: ${total_bill:.2f}')
            print(f'Each person should pay: ${bill_per_person:.2f}')


    # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage

    
    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).

    # NOTE: Calculate the tip and tax separately. 
     
    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.   
    
    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00

    # NOTE: The amounts are displayed with 2 decimals only

except: # TODO: modify this except to include a Built-in Exception
        total_cost = str

        # TODO: Print an statement telling the user their input is invalid 
        print('Your input is invalid')
    
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY
