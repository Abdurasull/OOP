# Vaqt nomli klassda soat, minut va sekund berilgan.

# Ya'na 3ta klass e'lon qiling va ular Vaqt klassiga bog'liq bo'lishi kerak:

# Hour nomli klass soatni 5ga oshiradi,

# Minut nomli klass minutni 5ga oshiradi va

# Sekund nomli klass sekundni 5ga oshiradi.

# O’zgargan vaqtni chiqaring.

class Vaqt:
    def __init__(self, Hours, menut, sekund):
        self.Hours = Hours
        self.menut = menut
        self.sekund = sekund


class Hours(Vaqt):
    def add_hours(Vaqt):
        Vaqt.Hours += 5

    
class Minut(Vaqt):
    def add_minut(Vaqt):
        Vaqt.menut += 5
    
class Sekund(Vaqt):
    def add_sekund(Vaqt):
        Vaqt.sekund += 5
        
vaqt = Vaqt(10, 10, 10)

Hours.add_hours(vaqt)

Minut.add_minut(vaqt)

Sekund.add_sekund(vaqt)

print(f"result:\nSoat: {vaqt.Hours}\nMinut: {vaqt.menut}\nSekund: {vaqt.sekund}")

