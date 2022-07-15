# Find sum of 
list1 = [1,2,[3]]
total = 0

def sum1(new_list):
    global total       # global keyword to modify variable outside of the current scope
    if new_list == []:  # base case to terminate
        return 0
    for i in range(len(new_list)):
        if type(new_list[i]) == int: 
            total = total + new_list[i]
        if type(new_list[i]) == list:  # if nested list do recursion
            sum1(new_list[i])   # pass list 
    return total    # final total

print(sum1(list1))

# o/p : 6

