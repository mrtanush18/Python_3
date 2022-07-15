# You are given 3 integers X, Y & Z representing the dimensions of a cuboid along with an integer N. 
# You have to print a list of all the possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k is not equal to n. 
# Here 0 <= i <= X , 0 <= j <= Y , 0 <= k <= Z.

x = int(input())
y = int(input())
z = int(input())
n = int(input())

coord = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]

# x + 1 makes range dynamic ex. if x = 3 loop will run 3 times 

print(coord)

# coord=[]

# for i in range(x+1):
#     # x = x + 1  --> not possible by compre
#     for j in range(y+1):
#         # y = y + 1
#         for k in range(z+1):
#             # z = z + 1
#             if i+j+k!=n:
#                 coord.append([i,j,k])