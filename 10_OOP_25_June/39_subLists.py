# Print all combinations of list elements
# o/p : [[],[4],[5],[6],[4,5],[4,6],[5,6],[4,5,6]]
# No class or Inheritance, Polymorphism, Composition needed as list has no attributes

class ListCombos:
    @classmethod
    def subList(s,list0):
        list2 = [[]]
        for i in range(len(list0)+1):  # range(4)
            for j in range(i):
                # print(list0[j:i])          
                list2.append(list0[j:i]) 
        ListCombos.printSubList(list2)

    @classmethod
    def printSubList(s,list2):
        print(list2)

    @classmethod
    def call(c,list0):
        ListCombos.subList(list0)
        

list0 = [4,5,6]

ListCombos.call(list0)

# o/p : [[], [4], [4, 5], [5], [4, 5, 6], [5, 6], [6]] ---> [4,6] not possible as its just slicing

# DRY RUN :  [j:i]
# print(list0[0:0]) # [] 
# print(list0[0:1]) # [4]
# print(list0[1:1]) # []
# print(list0[0:2]) # [4,5]
# print(list0[1:2]) # [5]
# print(list0[2:2]) # []
# print(list0[0:3]) # [4,5,6]
# print(list0[1:3]) # [5,6]
# print(list0[2:3]) # [6]

# [0:0], [1:1], [2:2] won't run as j in range(i)