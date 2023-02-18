class BOOK:
    def __init__(self):
        self.price = 50
        self.author = 'smarchx'
        self.title = 'Percy Jackson'
        self.pubyear = 2022

    def display(self):
        print(f'Title : {self.title} '
              f'Price : {self.price} '
              f'Author : {self.author} '
              f'Pubyear : {self.pubyear}')

obj1 = BOOK()
obj1.display()