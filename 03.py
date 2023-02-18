class Dog:
    Total = 0
    def __init__(self,Name,Age,Breed):
        self.Name = Name
        self.Age = Age
        self.Breed = Breed
        Dog.Total+=1

    def speak(self,sound):
        self.sound = sound
        print(self.sound)

    def defineDogSize(self,Hight):
        self.Hight = Hight
        if self.Hight > 80:
            print('Big Dog')
        elif self.Hight > 50 < 80:
            print(f'Standard Dog')
        else:
            print("Small Dog")

    def description(self):
        print(f'Name:{self.Name}\n Age:{self.Age}\n Breed:{self.Breed}\n')

    def count(cls):
        print(cls.Total)

obj1 = Dog('Shifu',18,'Shiba')
obj1.description()
obj1.speak('WOOF')
obj1.defineDogSize(90)
obj1.count()