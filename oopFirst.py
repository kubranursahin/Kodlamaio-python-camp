class book():
    def __int__(self, name, author, year, page):
        self.name = name
        self.author = author
        self.year = year
        self.page = page
b1Book = book()
b1Book.name = "Little Prince"
b1Book.author = "Antonie"
b1Book.page = 184
b1Book.year = 2000

print(b1Book.name, " ", b1Book.author, " ", b1Book.year, " ", b1Book.page)