# Keep revising these programs
> List > duplicatePrint, reverse_list, QuickReverseList, 
>

# Useful :
> TIP FOR JOB : Always find inbuilt methods to use in code like __del__ to reduce lines of code
> ord('A') returns ascii value of A  (functions : countCase)
> print(i, end = " ") to print o/p in single line 
> i**2 (sq of no)
> Multiline comment : '''
> int(input())
> Decrementing loop : for i in range(12, -1, -1): (start at 12, end at 0, decrement by -1)
> Array, string, object are user defined datatype unlike primitive types like int, float, string whose size is fixed
________________________________________________________________________________
# String : 
> Traverse : for i in string:
> To chk for empty string, use if string == '' (not ' ')
> To count words in string : count spaces + 1
> To reverse string str = str[::-1]
> To access last character of string : str[-1]
________________________________________________________________________________
# List :
> A list is defined as an ordered, mutable, and heterogeneous collection of objects.

> Traverse list : for i in list:
> Traverse Nested list : for i in range(len(list)): for j in list[i]:
> Chk if sth is in list : use flags
> Find item's exact index : if list[i] == toFind: pos = pos + i  # (pos = 1)
> To count sth : count variable declare globally
> Find unique items: create new list, compare both (not in) & append to new list
> Print duplicate items : use dict
> max_element = list[0] , sec_max_element = list[0] , 
if(max_element < element): 
if(sec_max_element < element and element != max_element):
> Reverse list : for i in range(length-1, -1, -1): temp = ogList[i] || reversed_list.append(temp)
                                                          i = 5 (last index)
> Quicker way: for i in range(len(list)//2): temp = list[0] || list[0] = list[-1]||list[-1] = temp || j = j - 1 = -1 -1 = -2
> Swap 1st & last elements in list : list[0],list[-1] = list[-1],list[0]
+ Imp : sumDigits.py : to find sum of digits of each no. in list convert to string 

> List Methods: 
list0.sort(), .append(), .extend(), x= max(list0), y= min(list0), len(list0),
list0.reverse(), list0.count(x) [count frequency of x in list]

for values in ogList:
    newList.append(pow(values,3))

# List comprehension:

________________________________________________________________________________
# Dictionary : 

> Create dict by taking i/p in same line : {k1:v1, k2:v2}
dict = {} 
size = int(input("No. of keys: "))
for i in range(size): 
    key , value = input("\nEnter key and value: ").split()
    dict[key] = value

# Create dynamic nested dict by taking i/p : {k1:{}, k2:{}}
dict = {}
size = int(input("No. of outer keys? "))
for i in range(size):
    outer_key = input('\nOuter key ')
    value = {}                          # Create new dict
    for j in range(2):                  # Input values in new dict
        key, val = input('\nEnter key & value: ').split()
    
        value[key] = val
        dict[outer_key] = value

# 3 lv nested dict : {key: {key1:{innermost key2 : value2}}, key1 : {innermost key2 : value2}}}

for i in range(2):
    outer_key = input('\nEnter outer key: ')  
    value = {}

    for j in range(1):  
        key1 = input('\nEnter inner key: ')  
        value1 = {}
        value[key1] = value1              

        dict[outer_key] = value         # IMP (TO AVOID OVERWRITING OF VALUES)  

        for k in range(2):
            key2 = input('\nEnter innermost key: ')  
            value2 = input('Enter innermost value: ')

            value1[key2] = value2

# Access values from super nested dict: 
for key,value in users_data.items():
    print(value)
    
    for k2,v2 in value.items():
        # print(v2)
        
        for k3,v3 in v2.items():
            # print(v3)
            temp = type(v3)      
            if temp == dict:
                
                for k4,v4 in v3.items():
                    # print(v4)
                    if type(v4) == list:
                        print(v4[0]['type'])

> Merge 2 dictionaries: for keys,values in dict2.items(): dict1.update(dict2)
> Sum of values of dict : for item in dict: sum = sum + dict[item]
> Concat keys of dict : for k in dict: key = key + str(k)

> Print                                 # or 
for k, v in dict.items():               for k in dict.keys():
    print(k,v)                              print(k,dict[k])

> Find duplicates
if j in dict2:
        dict2[j] = dict2[j] + 1
    else:
        dict2[j] = 1

_______________________________________________________________________________
# Comprehension : 
> Can't append in comprehension

> Walrus operator (:=)
ex:
sum = 0
sumList = [sum := sum + i for i in [1,2,3]]
________________________________________________________________________________
# Set
> No duplicate values allowed
> Index keeps changing (unordered), hence can't use for loop
________________________________________________________________________________
# Functions
> keywordParameters2 :
**kwarg & *arg
________________________________________________________________________________
# Recursion
> Base case : to terminate recursive fn calls & de-allocate memory 
> To draw stack tree or stack memory diag see where recursively fn is called

>> sumList.py : 
> global variable_name (use whenever you don't want variable reinitialized each time)
> type(new_list[i]) == list  (to find datatype)
> sum(list1[i]) doesn't work as it receives single element

> revString.py : 
s[1:]) 

> reverseList.py : 
[2] + [] == [2] 
________________________________________________________________________________
# Higher Order fns : Map, Reduce, Filter, Accumulate

> If facing many errors try writing fn normally without higher order fn

> PASS ITERABLE FIRST in accumulator fn (sumListAccumulate)

        Map                                        Reduce
1) Each element is changed                  1) Not each element is changed
2) Relation bw elements not maintained      2) Relation maintained
3) Returns object (all items)               3) Returns single element as o/p
4) Requires typecasting of o/p              4) Does not need typecasting
5) Inbuilt fn can be passed                 5) Can be passed, usually write own fn
(ex. splitStringMap.py)
5) Applications: cube / double List,        5) max / min of list, sum of nested list
len(string) in list, round off list items
sum lists

> Lambda fn or anonymous fn can be used in all higher order fns or independently