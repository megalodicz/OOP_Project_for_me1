class BOOK:
    def __init__(self):
        self.__price = 100
        self.__author = 'smarchx'
        self.__title = 'Percy Jackson'
        self.__pubyear = 2022

    def calBookPrice(self):
        print(((100*0.07))+self.__price)

    def recomendNewBook(self):
        if self.__pubyear - 2022 <=1 :
            print('New book')
        else:
            print('Old book')

    def settitle(self, newtitle): #Setter
        self.__title = newtitle

    def gettitle(self):
        print(self.__title) #Getter

    def display(self):
        print(f'Title : {self.__title} '
              f'Price : {self.__price} '
              f'Author : {self.__author} '
              f'Pubyear : {self.__pubyear}')

obj1 = BOOK()
obj1.display()
obj1.calBookPrice()
obj1.recomendNewBook()