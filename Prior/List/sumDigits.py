# Print sum of each element of list ex. 12 --> 1 + 2 = 3

list = [12,41,39,57,90]

num_string = []

for i in list:
    string = str(i)  # convert each int item to a string for indexing
    sum = 0          # reset sum to 0 after each iteration

    for j in string:        
        sum = sum + int(j)  # sum = sum + 1, next sum = 1 + 2 = 3
    num_string.append(sum)  # only append final sum 

print(num_string)

# o/p:
# [3, 5, 12, 12, 9]

# ____________________________________________________________________________________
# How to think of solution to problem ??
# --> list = [12,41,39,57,90]
# Elements are of datatype int and in int we can't access digits individually so we cast int to string in which we get index for each digit.
# Then we can add digits of each number to sum variable and then we need to append sum value into another list. 
# Then we need to reset sum for next iteration so we write it inside outer for loop
