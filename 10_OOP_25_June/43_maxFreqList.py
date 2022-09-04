# Find element in list occuring most
# # No constructor or Inheritance, Polymorphism, Composition needed as list has no attributes

class MaxFreq:
    @classmethod
    def listToDict(s,list0):
        dict1 = {}  

        for i in list0:
            if i in dict1:
                dict1[i] = dict1[i] + 1
            else:
                dict1[i] = 1

        MaxFreq.findMaxFreq(dict1) 

    @classmethod
    def printMaxValues(s,max,dict1):
        for k,v in dict1.items():
            if v == max:
                print(k, ":", v)

    @classmethod
    def findMaxFreq(s,dict1):
        values = []
        for v in dict1.values():
            values.append(v)

        # print(values)

        MaxFreq.printMaxValues(max(values), dict1)

    @classmethod
    def call(c,list0):
        MaxFreq.listToDict(list0)


list0 = [2,3,4,3,2,5,6,7,6,5,6]
MaxFreq.call(list0)

# o/p : 6 : 3
