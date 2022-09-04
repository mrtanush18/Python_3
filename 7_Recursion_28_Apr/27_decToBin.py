# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

convertToBinary(34)  # decimal number

'''
34 // 2 = 17    34 % 2 = 0
17 // 2 = 8     17 % 2 = 1
8 // 2 = 4      8 % 2 = 0
4 // 2 = 2      4 % 2 = 0
2 // 2 = 1      2 % 2 = 0
1 % 2 = 1 
'''