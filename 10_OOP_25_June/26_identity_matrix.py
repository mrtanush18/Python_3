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

        for i in range(len(s.result)):
            for j in range(len(s.result[i])):
                if (i+1) == (j+1):
                    s.result[i][j] = 1
                
        for r in s.result:
            # print('r')
            print(r)

obj1 = matrix()

obj1.showResult()

'''
o/p:

[1, 15, 4]
[10, 1, 9]
[11, 13, 1]

'''