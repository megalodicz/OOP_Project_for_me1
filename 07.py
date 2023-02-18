class Document:
    def __init__(self,authors,date):
        #self.authors = []
        #self.authors.append(authors)
        self.authors = list(authors)
        self.date = date

    def getAuthors(self):
        print(self.authors)

    def addAuthors(self,NewAuthors):
        self.authors.append(NewAuthors)

    def getDate(self):
        print(self.date)

class Book(Document):
    def __init__(self,title):
        self.title = title

    def getTitle(self):
        print(self.title)

class Email(Document):
    def __init__(self,subject,to):
        self.subject  = subject
        self.to  = list(to)

    def getSubject(self):
        print(self.subject)

    def getTo(self):
        print(self.to)
