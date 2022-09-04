num = int(input())

def chkRange(num):
    list= []
    for i in range(5,11): # create a list of items from 5 to 11
        list.append(i)
    # print(list)

    if num in list:
        print("Yes within range") 
    else:
        print("No not within range")

chkRange(num)

# o/p : 5
# Yes within range