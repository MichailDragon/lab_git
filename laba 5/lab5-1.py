class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

# title = input('Напишите название: ')
# author = input('Напишите автора: ')
# year = input('Напишите год: ')

# my_book = Book(title, author, year)

my_book1 = Book("Первый", "Михаил Владимирович Савич", "2016")

r = my_book1.get_info()
print(r)
