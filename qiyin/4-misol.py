# Talabalar o'rtasida stipendiya tayinlash haqida masala yarating.
# Class elementi quyidagilar bo'lsin:

# Talaba ismi;
# O'rtacha bahosi;
# Davlat granti yoki kontrakt asosida o'qishi;
# Stipendiya miqdori.
# Class ichida kiritish va chiqarish methodlarini yozing. 5 ta obyekt yarating va faqat davlat grantida o'qiydigan va o'rtacha bahosi 85 dan yuqori bo'lgan talabalar stipendiya miqdorini chiqaring.

class Student_stependiya:
    def __init__(self, name, ball, daraja, stependiya):
        self.name = name
        self.ball = ball
        self.daraja = daraja
        self.stependiya = stependiya

    def sort(self):
        if self.daraja == "Grant" and self.ball >= 85:
            print(f"Ism: {self.name}\nDarajasi: {self.daraja}\nO`rtacha ball: {self.ball}\n\n")
list_inst = []
list_inst.append(Student_stependiya("Asror", 85, "kantrakt", 1_000_000))              
list_inst.append(Student_stependiya("Suxrob", 90, "Grant", 2_000_000))              
list_inst.append(Student_stependiya("Olim", 70, "kantrakt", 3_000_000))              
list_inst.append(Student_stependiya("Eldor", 87, "Grant", 3_000_000))              
list_inst.append(Student_stependiya("Abdulaziz", 85, "kantrakt", 2_000_000))              

for ins in list_inst:
    ins.sort()