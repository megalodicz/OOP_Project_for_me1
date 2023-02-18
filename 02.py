class Species:
    count = 0
    def __init__(self,brand,model,gas_tank_size):
        self.brand = brand
        self.model = model
        self.gas_tank_size = gas_tank_size
        Species.count+=1

    def fuel_up(self):
        if self.gas_tank_size == 10:
            print('FULL')
        elif self.gas_tank_size > 2:
            print('NORMAL')
        elif self.gas_tank_size <= 2:
            print('QUITE EMPTY')
        elif self.gas_tank_size ==0:
            print('EMPTY')

    def showcount(cls):
        print(cls.count)


    def show(self):
        print(f'Brand :{self.brand} '
              f'Model :{self.model} ')


obj1 = Species('Honda','Y',9)
obj2 = Species('SUbaru','x',5)
obj1.showcount()
obj1.show()
obj1.fuel_up()