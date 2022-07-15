months = ['January', 'February', 'March'] 
prices = [238.11, 237.81, 238.91]

min_price = min(prices)  # min(list_name)

# print(min_price)

min_index = prices.index(min_price)   #list_name.index(toFind)

# print(min_index)

min_month = months[min_index]  # []

# print(min_month)

# extend

months.extend(prices)

# print(months)

# copy

fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
# print(x)