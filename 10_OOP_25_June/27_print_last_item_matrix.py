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
        for i in range(len(s.X)):
            for j in range(len(s.X[i])):
                if j == len(s.X[i])-1:
                    print(s.X[i][-1])

obj1 = matrix()

obj1.showResult()

'''
o/p:
3
6
9
'''