from datetime import datetime
# Metodlar:
# add_item(name, price) — yangi mahsulotni qo‘shadi.
# remove_item(name) — mahsulotni savatdan o‘chiradi.
# get_total() — savatdagi mahsulotlarning jami narxini hisoblaydi.
# Masalan:
# Mahsulotlar qo‘shilgach, foydalanuvchi get_total() metodini chaqiradi. Savatning umumiy narxi qaytarilishi kerak.

class ShoppingCart:
    Product = {}
    def __init__(self):
        self.product_list = []

    def add_item(self, name: str, price: float):
        self.Product = {'name': name, 'price': price}
        if self.Product not in self.product_list:    
            self.product_list.append(self.Product)
            hozzirgi_vaqt = datetime.now()
            result_time = hozzirgi_vaqt.strftime("%Y-%m-%d  %H:%M:%S")
            with open("date.txt", "a") as file:
                file.write(f"Savatga solingan vaqt {result_time}\nMahsulot nomi: {self.Product['name']}\nMahsulot narxi: {self.Product['price']}\n\n")
        else:
            print(f"{self.Product['name']} ni savatga solib bo`lganingiz uchun yana qayta solmadik :)\n")
    def remove_product(self, name: str):
        if self.product_list:
            for prouct in self.product_list:
                if prouct['name'] == name:
                    self.product_list.remove(prouct)

    def kassa(self):
        sum = 0
        if len(self.product_list) != 0:
            for product in self.product_list:
                sum += product['price']
            print(f"Umumiy harid: {sum} sum")
        else:
            print("Kechirasiz, savatingiz bumbush ekan :(")

# shop1 nomli obyekt yaratib olamiz
shop1 = ShoppingCart()

# unga maxsulotlar qo`shamiz
shop1.add_item("Olma", 5000)
shop1.add_item("Sok", 8000)
shop1.add_item("anor", 15000)
shop1.add_item("Olma", 5000)

# har bir qo`shilgan maxsulotni terminalda chop etamiz
print("Savatdagi maxsulotlar")
for maxsulot in shop1.product_list:
    print(f"Maxsulot nomi: {maxsulot['name']}\nmaxsulot narxi: {maxsulot['price']}")


# maxsulotni savatdan olib tashlaymiz
shop1.remove_product("Olma")

# va yana natijani solishtiramiz
print("\nSavatdagi maxsulotlar")
for maxsulot in shop1.product_list:
    print(f"Maxsulot nomi: {maxsulot['name']}\nmaxsulot narxi: {maxsulot['price']}")

#Umumiy haridni bahosini hisonlaymiz
shop1.kassa()
