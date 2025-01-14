
#   Xodimlarni boshqarish (Manager) class yarating.
# Elementlari:

# Xodim ismi;
# Lavozimi;
# Ish vaqti (soat);
# Ish haqi.
# Shart:

# 7 ta obyekt yarating.
# Ish vaqti 40 soatdan yuqori va lavozimi "Rahbar" bo‘lgan xodimlarni ro‘yxatga oling.

class Xodimlar:
    def __init__(self, name, lavozim, time_work, ish_haqqi):
        self.name = name
        self.lavozim = lavozim
        self.time_work = time_work
        self.ish_haqqi = ish_haqqi

    def sort(self):
        if self.time_work > 40 and self.lavozim == 'Raxbar':
            print(f"Ishchining nomi: {self.name}\nIshdagi lavozimi: {self.lavozim}\nIsh haqqi: {self.ish_haqqi}\n\n")
list_inst = []
list_inst.append(Xodimlar("Abror", "Raxbar", 46, 15_000_000))              
list_inst.append(Xodimlar("Akbar", "Menadger", 42, 10_000_000))              
list_inst.append(Xodimlar("Xalima", "Farrosh", 36, 5_000_000))              
list_inst.append(Xodimlar("Baxrom", "Raxbar", 50, 18_000_000))              
list_inst.append(Xodimlar("Asror", "Raxbar", 46, 12_000_000))              
list_inst.append(Xodimlar("Suxrob", "Dasurchi", 20, 15_000_000))              
list_inst.append(Xodimlar("Elbek", "Kotib", 46, 8_000_000))               
for ins in list_inst:
    ins.sort()