#  IMP : 5) Reverse string str[::-1], 6) Reverse items in list

# 1) Use list comprehension to print even nos. from 1 to 10 ___________________________________________________________________________________________________
even_numbers = [i for i in range(1,11) if i%2 == 0]
print(even_numbers)

# o/p : [2, 4, 6, 8, 10]___________________________________________________________________________________________________
# 2) Print nos from 1 to 50 which are divisible by 2 and 5 ___________________________________________________________________________________________________
divisible = [i for i in range(1,51) if i%2 == 0 and i%5 == 0]
print(divisible)

# o/p : [10, 20, 30, 40, 50]___________________________________________________________________________________________________
# 3) Print odd and even nos from 0 to 10 ___________________________________________________________________________________________________
odd_even = ["even" if i%2 == 0 else "odd" for i in range(0,11)]
print(odd_even)

# o/p : ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']___________________________________________________________________________________________________
# 4) Print word in list that ends with b and has length > 2 ___________________________________________________________________________________________________
list = ['Ch','Dh','Eh','cb','Tb','Td','Chb','Tdb']

word = [i for i in list if len(i) > 2 and i[-1] == 'b']
print(word)

# o/p : ['Chb', 'Tdb']
# ___________________________________________________________________________________________________
# 5) Reverse string 
# ___________________________________________________________________________________________________
# str = 'python'
# print(str[::-1])

# o/p : nohtyp 
# ___________________________________________________________________________________________________
# 6) Reverse items in list 
# ___________________________________________________________________________________________________
# list[('Java','Python','PHP')]  # tuple inside list

# reversed_items = [i[::-1] for i in ('Java','Python','PHP')]

# print(reversed_items)

# o/p : ['avaJ', 'nohtyP', 'PHP']

# WRONG: reversed_items = [temp for i in list length = len(i) while(length>=0) temp = "" + i[length-1] length - 1]___________________________________________________________________________________________________
# 7) Add item to next item in list ___________________________________________________________________________________________________
# list = [1,2,3]

# EASY Method  : 
# sum = 0
# sumList = [sum := sum + i for i in [1,2,3]]
# print(sumList) 

# Hard Method : 
# sumList = [sum(list[:i+1]) for i in range(len(list))]
# print(sumList)

# o/p : [1, 3, 6]
# ___________________________________________________________________________________________________
# 8) Calculate square of nos from 0 to 1 million. Which executes faster : list comprehension or normal way ?
# ___________________________________________________________________________________________________

## To find sq of nos from 0 to 10 :
# res = [i**2 for i in range(pow(10,1))]
# print(res)

# import time
# begin = time.time()
# res = [i**2 for i in range(pow(10,6))]
# end = time.time()
# print("Time taken by list comprehension: ",end-begin) 

# o/p : Time taken by list comprehension:  0.28731369972229004

# ___________ NORMAL WAY ___________

# import time
# begin = time.time()
# squared = []
# value = pow(10,6)

# for i in range(value):
#     sq = pow(i,2)
#     squared.append(sq)

# end = time.time()

# print("Time taken: ",end-begin)

# print(squared)  # no need to print as measuring time 

# o/p : Time taken:  0.3924398422241211 ___________________________________________________________________________________________________

# 9) Concat items in list into a single string ___________________________________________________________________________________________________
# list = ['I', 'want', 2, 'python', 'books']

# sum = ""
# sentence = [sum := sum + " " + str(i) for i in list]
# print(sentence[-1])

# o/p :  I want 2 python books ___________________________________________________________________________________________________

# 10) Split string into individual characters ___________________________________________________________________________________________________
# separated_characters = [i for i in 'Dictionary']

# print(separated_characters)

# NORMAL WAY :

# string = "Dictionary"
# list = []

# for i in string:
#     list.append(i)

# print(list)

# o/p : ['D', 'i', 'c', 't', 'i', 'o', 'n', 'a', 'r', 'y'] 
