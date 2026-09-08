#Library class

class library():
    def __init__(self):
       self.store = {}

    def add_book(self, book, author):
       if "books" not in self.store:
          self.store["books"] = []
       self.store["books"].append(book)

       if "authors" not in self.store:
          self.store["authors"] = []
       self.store["authors"].append(author)

    def show_book(self):
       for book, author in  zip(self.store["books"], self.store["authors"]):
          print(f"{book} by {author}")

#Storage 

    def save(self,filename):
        with open(filename, 'w') as file:
            for book, author in zip(self.store["books"], self.store["authors"]):
                file.write(str(f"{book} by {author}\n"))
               
    def load(self, filename):
        with open(filename, 'r') as file:
            return file.read()
