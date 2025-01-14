
class Instrument:
    def __init__(self, name, price, name_comp, Type_inst):
        self.name = name
        self.price = price
        self.name_comp = name_comp
        self.type_ins = Type_inst

    def sort(self):
        if self.price > 2_000_000 and self.type_ins == 'klaviatura':
            print(f"Instrument nomi: {self.name}\nIshlab chiqarilgan kompaniyasi: {self.name_comp}\nNarxi: {self.price}\n\n")
list_inst = []
list_inst.append(Instrument("Pyanina", 6_000_000, "KPR", "klaviatura"))              
list_inst.append(Instrument("Dumbura", 500_000, "Uz", "Udarcha"))              
list_inst.append(Instrument("Nay", 300_000, "Kz", "FUF"))              
list_inst.append(Instrument("Gitara", 3_000_000, "shvit", "TingTing"))              
list_inst.append(Instrument("Dutor", 6_000_000, "KPR", "klaviatura"))              
list_inst.append(Instrument("Tuba", 2_000_000, "KPR", "Fuf"))              
list_inst.append(Instrument("Champ", 2_200_000, "KPR", "klaviatura"))               
for ins in list_inst:
    ins.sort()