# Doesn't use inheritance or composition
# Add r1c1 with r1c2 in a 3x3 matrix : [[1,2,3],[4,5,6],[7,8,9]] using OOP

class matrix:
    def __init__(self):
        self.X = [[12,7,3],
                  [4 ,5,6],
                  [7 ,8,9]]

        self.Y = [[5,8,1],
                  [6,7,3],
                  [4,5,9]]

        self.result = [[0,0,0],
                       [0,0,0],
                       [0,0,0]]

    def showResult(s):
        # iterate through rows
        for i in range(len(s.X)):
        # iterate through columns (inner lists)
            for j in range(len(s.X[0])):
                s.result[i][j] = s.X[i][j] + s.Y[i][j]

        for r in s.result:
            print(r)

obj1 = matrix()

obj1.showResult()


'''
o/p: 

[17, 15, 4]
[10, 12, 9]    
[11, 13, 18]   
'''