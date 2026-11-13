

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

   
    def show_info(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)


    def borrow_book(self):
        if self.available == True:
            self.available = False
            print("Book borrowed successfully")
        else:
            print("Sorry! Book is not available")

    def return_book(self):
        if self.available == False:
            self.available = True
            print("Book returned successfully")
        else:
            print("This book was not borrowed")



book1 = Book("Python for Kids", "Jason")
book2 = Book("Animal World", "David")
book3 = Book("Space Adventure", "Alex")



books = []

books.append(book1)
books.append(book2)
books.append(book3)




print(" all book informaation ")

for book in books:
    book.show_info()
    print()


print("boorrow first book")
book1.borrow_book()


print("\n borrrow first book again ")
book1.borrow_book()


print("\n return first book")
book1.return_book()


print("\n show book information")
book1.show_info()
