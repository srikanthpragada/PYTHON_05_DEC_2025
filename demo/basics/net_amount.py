# Take qty and price and displays net amount after a discount of 10%

#input
price = int(input("Enter price :"))
qty = int(input("Enter qty :"))

#process
amount = price * qty
discount = amount * 10 // 100
net_amount = amount - discount

#output
print(f'Amount     : {amount:6}')
print(f'- Discount : {discount:6}')
print(f'Net Amount : {net_amount:6}')

