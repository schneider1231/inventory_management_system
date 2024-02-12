menu = [] 
stock = {}
price = {}


# Get the number of items on the menu from the user
menu_len = int(input("Enter number of items on the menu : "))

# Add to the menu list with user-inputted items
for i in range(menu_len):
    item = input("Enter Menu Item: ")
    menu.append(item)

# Add to the stock amounts with user-input for each menu item
for i in range(menu_len):
    name = menu[i]
    stock_total = float(input(f"Enter stock amount for {name}: "))

    stock[name] = stock_total

# Add to the price dictionary with user-inputted prices for each menu item
for i in range(menu_len):
    name = menu[i]
    item_price = float(input(f"Enter item price for {name}: "))

    price[name] = item_price

# Calculate the total stock value 
stock_total = sum(stock[item] * price[item] for item in stock)

# Print each item in the stock dictionary along with its stock amount and price
for item in stock:
    print(f"Item: {item} stock: {stock[item]} price: {price[item]}\n")
    
print(f"Total stock value is £{stock_total}")
