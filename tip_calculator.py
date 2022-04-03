# created a variable name and assign the string Ms. Johnson
# print how was your meal and here's the bill no rush with customer name
customer_name = ('Ms. Johnson')
print(f'How was your meal and here is the bill no rush {customer_name}. ', '\n')

# get the total bill amount for the customer to calculate tip
# created a variable name bill equals to a input as a float for the user to enter the total bill amount
bill = float(input('Total bill amount: '))

# created a tip variable tip equals an input as a integer for the user to 'enter tip percentage' using the (%) - modulus operator
tip = int(input('Enter tip percentage (%): '))

# created a people variable peolpe equals an input as a integer for the user to enter 'split by how many'
people = int(input('Split by how many: '))

# created a bill before tip variable equals what the bill is including the tip inputed
bill_before_tip = bill * (tip/100 + 1)

# created a tax variable equals the bill multiplied by a 10% tax thats repersented by .1
tax = bill * .1

# created a final bill variable equals to the bill total plus tax
final_bill = bill_before_tip + tax

# created a split variable equals to the final bill divided by the number of people inputed
split = "{:,.2f}".format(final_bill / people)

# printing the total bill to pay with tax and tip
print(f'Total bill to pay: ${final_bill}', '\n')

# printing the split total for each person to pay at the dinner party
print(f'Each person owes ${split} towards dinner with tax and tip', '\n')

print("Thank you for dining with us.", '\n')
