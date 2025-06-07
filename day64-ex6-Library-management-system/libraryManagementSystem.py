# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
  def __init__(self, books):
    self.books = books
    self.no_of_books = len(self.books)
    
  def show_books(self):
    print(f"Books in Library:", self.books)
    
  def add_books(self, book):
    self.books.append(book)
    self.no_of_books = len(self.books)
    print(f"{book} is add into the Library")
  
  def get_no_of_books(self):
    print(f"Total number of books is: {self.no_of_books}")
  
a = Library(["Harray portter", "1965"])
a.show_books()
a.get_no_of_books()
a.add_books("Ego")
a.show_books()
a.get_no_of_books()