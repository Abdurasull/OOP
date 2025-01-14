from colorama import Fore, Style, Back
# Telefon nomi;
# Telefon RAM hajmi;
# Narxi;
# Ishlab chiqaruvchi kompaniya.

class Phon:
    def __init__(self, name: str, hotira: int,  price: float, name_comp: str):
        self.name = name
        self.hotira = hotira
        self.price = price
        self.name_comp = name_comp
    def measure(self):
        if self.hotira > 2 and self.hotira < 8:
            print(f"{Fore.YELLOW}{self.name}, {self.name_comp}, {self.hotira} GB, {self.price} ${Fore.RESET} ")
        else:
            print(f"{Fore.RED}Kechirasiz biz bu telefon qaqida sizga ma`lumot bera olmaymiz{Fore.RESET}")
            return
phon1 = Phon("Samsung_A51", 5, 400, "Samsung")
phon2 = Phon("Iphon_15", 16, 1100, "Apple")

phon1.measure()
phon2.measure()
