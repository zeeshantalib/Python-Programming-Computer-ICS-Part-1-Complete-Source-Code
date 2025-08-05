# Title: Book Information without Constructor

class Book:
    def set_details(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)

b1 = Book()
b1.set_details("Python Basics", "Zeeshan Talib", 250)
b1.show_details()

# Output:
# Title: Python Basics, Author: John Smith, Pages: 250
