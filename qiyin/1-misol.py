from datetime import datetime

class Book:
    
    def __init__(self, name_book, author):
        self.name_book = name_book
        self.author = author
        self.borrower = None
        self.due_date = None

    def borrow(self, name, date):
        # Kitobni qarzga olish.
        if self.borrower:
            print(f"Kitob allaqachon {self.borrower} tomonidan qarzga olingan.")
        else:
            self.borrower = name
            self.due_date = datetime.strptime(date, '%Y-%m-%d')
            print(f"{self.name_book} kitobi {name} tomonidan {date} sanasiga qadar qarzga olindi.")

    def return_book(self):
        if not self.borrower:
            print("Bu kitob qarzga olinmagan.")
            return
        
        today = datetime.today()
        if self.due_date and today > self.due_date:
            print("Jazo qullaniladi!")
        else:
            print("Kitob vaqtida qaytarilgan. Rahmat!")
        
        
        self.borrower = None
        self.due_date = None


book = Book("Vavlionning eng boy kishisi", "John")

book.borrow("Abdurasul", "2025-01-20")
book.return_book()

book.borrow("Doston", "2025-01-20")

# Qaytarish muddatini o'tkazib yuborgan holatda sinab ko'rish:
book.borrow("Ali", "2025-01-10")
book.return_book()