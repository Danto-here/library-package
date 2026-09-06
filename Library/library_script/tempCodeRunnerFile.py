import ast


#Library class

class Library():
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

#Storage system

file_name = "Read_books.txt" #Can be changed to whatever you like(do not remove the .txt though)

def save(filename, data):
   with open(filename, 'w') as file:
      file.write(str(data))

def view(filename):
   with open(filename, 'w') as file:
      file.read(filename)
