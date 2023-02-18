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



obj1 = Student('Jarkapat',[89,94,45,56,])
obj2 = Student('Mathat',[55,78,34,90])
obj2.avgScore()
obj2.show()
obj1.addScore(10)
obj1.avgScore()
obj1.show()
obj1.Showall()
#obj1.avgScore()
#obj1.Showall()
