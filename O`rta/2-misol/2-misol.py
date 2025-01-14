# Restaurant nomli classdan FastFood (tez ovqatlanish) va
# FineDining (yuqori darajadagi restoran) vorislarini hosil qiling. 
# Har birining menyusi va narxlarini ifodalovchi metod bo'lsin.

class Restorand:
    menu = []
    Food = {}
    def __init__(self, name: str):
        self.name = name
        self.menu = []
    def add_food(self, name: str, price: int ):
        self.Food = {'name': name,
                     'price': price
                    }
        self.menu.append(self.Food)

class FastFood(Restorand):
    def __init__(self, name):
        super().__init__(name)

class FineDining(Restorand):
    def __init__(self, name):
        super().__init__(name)

# FastFood1 restorani
FastFood1 = FastFood("FastFood")
FastFood1.add_food("chekkin 1kg", 65000)
FastFood1.add_food("Kartofil 1kg", 35000)
d = 0
print(FastFood1.name)
for menu in FastFood1.menu:
    d +=1
    print(f"{d} - taom: {menu['name']} va narxi {menu['price']}")

# FineDining1 restarani
FineDining1 = FineDining("FineDining")
FineDining1.add_food("Shashlik 1kg", 110000)
FineDining1.add_food("Osh 1kg", 70000)
d = 0
print(FineDining1.name)
for menu1 in FineDining1.menu:
    d +=1
    print(f"{d} - taom: {menu1['name']} va narxi {menu1['price']}")
    

