from itertools import combinations

def sub_lists(my_list):
    subs = []
    for i in range(0, len(my_list)+1):
        temp = [list(x) for x in combinations(my_list, i)]
        print("temp: ",temp)
        subs.extend(temp)
    return subs


l1 = [4, 5, 6]
print("Original list:")
print(l1)
print("Sublists of the said list:")
print(sub_lists(l1))

# o/p : [[], [4], [5], [6], [4, 5], [4, 6], [5, 6], [4, 5, 6]]