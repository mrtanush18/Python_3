# 9) Concat items in list into a single string ___________________________________________________________________________________________________
list = ['I', 'want', 2, 'python', 'books']

sum = ""
sentence = [sum := sum + " " + str(i) for i in list]
print(sum.strip())

# o/p :  I want 2 python books 