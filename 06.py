class Student:
    all_student = 0
    avg_Point = []

    def __init__(self,Name,Point):
        self.Name = Name
        self.Point = list(Point)
        Student.all_student+=1


    def addScore(self,NewScore):
        self.NewScore = NewScore
        self.Point.append(self.NewScore)

    def show(self):
        print(self.Name,(self.Point))

    def avgScore(self):
        self.avg = (sum(self.Point)/len(self.Point))
        Student.avg_Point.append(self.avg)
        print(self.avg)

    def Showall(cls):
        print(cls.all_student,sum(cls.avg_Point)/len(cls.avg_Point))

    def calGrade(self):
        self.cal = int(self.avg//10)
        print(self.cal)
        self.G = 'FFFFFDCBAAA'
        print(self.G[self.cal])

obj1 = Student('Jarkapat',[100,100,100,100])
obj1.addScore(10)
obj1.avgScore()
obj1.show()
obj1.calGrade()
