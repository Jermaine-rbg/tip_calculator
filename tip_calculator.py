# create a variable name and assign the string Ms. Johnson
# print how was your meal and here's the bill no rush with customer name
customer_name = ('Ms. Johnson')
print(f'How was your meal and here is the bill no rush {customer_name}. ', '\n')

# get the total bill amount for the customer to calculate tip
# next create a variable name bill equals to a input as a float with text enter the total bill amount
bill = float(input('Total bill amount: '))

# create a variable tip equals an input as a integer with the text 'enter tip percentage' using the (%) - modulus
tip = int(input('Enter tip percentage (%): '))

# create a variable peolpe equals an input as a integer with text 'split by how many'
people = int(input('Split by how many: '))

bill_before_tip = bill * (tip/100 + 1)

tax = bill * .1

final_bill = round(bill_before_tip + tax, 3)

split = round(final_bill / people)

print(f'Total bill to pay: ${final_bill}', '\n')

print(f'Each person owes ${split} towards dinner with tax and tip')
