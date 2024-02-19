#Compulsory Task 1
'''
create list with four items
create dictionary with items' cost
create dictionary with items' price
calculate total_stock worth in your cafe
    use for loop to get item price and count
    multiply these together
    add iteratively to total worth
    print value per item
print total value of items in cafe
'''

menu = ['sandwich', 'cake', 'water', 'tea']
stock_value = {'sandwich': 30, 'cake': 30, 'water': 50, 'tea': 100}
stock_price = {'sandwich': 5, 'cake': 3, 'water': 2, 'tea': 1.50}

total_stock_worth = 0

for each_item in menu:
    item_price = stock_price[each_item]
    item_count = stock_value[each_item]
    total_value = item_count * item_price
    total_stock_worth += total_value
    print(f'The total value of {each_item} is {total_value}')

print(f'Total value of the stock in the cafe is: {total_stock_worth}')





