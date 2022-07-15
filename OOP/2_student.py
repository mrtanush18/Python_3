# class that takes i/p student details & displays them

class student:
    def __init__(self):
        self.name = ""      # common default values for all objs
        self.roll = 0
        self.total = 0
        self.all_subj = []
        self.grade = "" 
        self.percent = 0    
    
    def calcTotal(a):
        a.total = sum(a.all_subj)
        print("Total marks: ",a.total)
    
    def calcPercent(p):
        p.percent = (p.total/400)*100
        print("Percentage: ",p.percent,"%")

    def getGrade(self):
        if self.percent > 0 and self.percent < 40:
            self.grade = 'D'
        if self.percent > 40 and self.percent < 50:
            self.grade = 'C'
        if self.percent > 50 and self.percent < 75:
            self.grade = 'B'
        if self.percent > 75:
            self.grade = 'A'
        print("Grade: ",self.grade)

    def setDetails(s):
        s.name = input('Enter name: ')
        s.roll = int(input('Enter roll no: '))
        for i in range(5):
            s.all_subj.append(int(input('Enter marks: ')))

    def showDetails(self):  # API, uses abstraction
        print(self.all_subj)
        self.calcTotal()
        self.calcPercent()
        self.getGrade()
    

# objects

s_1 = student()

s_1.setDetails()

s_1.showDetails()

'''
o/p:
Enter name: sam
Enter roll no: 18
Enter marks: 32
Enter marks: 40
Enter marks: 50
Enter marks: 60
Enter marks: 70
[32, 40, 50, 60, 70]
Total marks:  252
Percentage:  63.0
'''

