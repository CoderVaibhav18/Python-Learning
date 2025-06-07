# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
  def __init__(self, books=None):
    if books is None:
      self.books = [] 
    else:
      self.books = books
    self.no_of_books = len(self.books)
    
  def show(self):
    print("Books in library:", self.books)
    
  def add_books(self, book):
    self.books.append(book)
    self.no_of_books = len(self.books)
    print(f'"{book}" added to the library.')
    
  def get_no_of_books(self):
    print("Number of books:", self.no_of_books)
    
a = Library(["Harry Potter", "vaibhav"])
a.show()
a.get_no_of_books()
a.add_books("sathe")
a.show()
a.get_no_of_books()