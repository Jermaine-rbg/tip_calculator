# created a variable name and assign the string Ms. Johnson
# print how was your meal and here's the bill no rush with customer name
customer_name = ('Ms. Johnson')
print(f'How was your meal and here is the bill no rush {customer_name}. ', '\n')

# get the total bill amount for the customer to calculate tip
# next create a variable name bill equals to a input as a float with text enter the total bill amount
bill = float(input('Total bill amount: '))

# created a tip variable tip equals an input as a integer with the text 'enter tip percentage' using the (%) - modulus
tip = int(input('Enter tip percentage (%): '))

# created a people variable peolpe equals an input as a integer with text 'split by how many'
people = int(input('Split by how many: '))

# created a bill before tip variable equals what the bill is including the tip 
bill_before_tip = bill * (tip/100 + 1)

# created a tax variable equals the bill multiplied by a 10% tax thats repersented by .1
tax = bill * .1

# created a final bill variable equals to the rounded bill total plus tax
final_bill = round(bill_before_tip + tax, 3)

# created a split variable equals to the rounded final bill divided by the number of people
split = round(final_bill / people)

# printing the total bill to pay with tax and tip
print(f'Total bill to pay: ${final_bill}', '\n')

# printing the split total for each person to pay at the dinner party
print(f'Each person owes ${split} towards dinner with tax and tip', '\n')

# giving the customer the option to add another tip
# created a if elif statement to enter yes or no for additional tip
# if Yes please re-run the tip calculator 
# if No the print statment will output have a great day

additional_tip = input('Would you like to enter another tip? (Yes/No) \n')
if additional_tip == 'Yes':
    bill_before_tip()
elif additional_tip == 'No':
    print("Have a great day!")