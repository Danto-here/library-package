from library_script import Library

file_name = "Test.txt"

lib = Library()

lib.add_book("Ulysses", "James Joyce")
lib.add_book("1984", "George Orwell")
lib.add_book("Solo Leveling", "Chugong")

lib.save(file_name)
lib.load(file_name)