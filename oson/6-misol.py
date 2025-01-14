from colorama import Fore, Back, Style

class Mashina:
    def __init__(self, marka: str, modil: str, yil: int, narxi: int):
        self.marka = marka
        self.modil = modil
        self.yil = yil
        self.narxi = narxi
    def produced(self):
        if self.yil > 2010:
            print(f"{Fore.GREEN}{self.marka}, {self.modil}, {self.yil} da ishlangan narxi {self.narxi}${Fore.RESET}")
mashenakr_bazasi = []
Mashina1 = Mashina('chevrolit', 'Nixa 3', 2018, 10000)
mashenakr_bazasi.append(Mashina1)
Mashina2 = Mashina('chevrorit', 'cobolt', 2013, 9000)
mashenakr_bazasi.append(Mashina2)
Mashina3 = Mashina('Cherry', 'M6_x1', 2018, 18000)
mashenakr_bazasi.append(Mashina3)
Mashina4 = Mashina('chevrolit', 'matiz', 2009, 3000)
mashenakr_bazasi.append(Mashina4)
Mashina5 = Mashina('Laccitti', 'Spark', 2019, 8000)
mashenakr_bazasi.append(Mashina1)

for mashina in mashenakr_bazasi:
    mashina.produced()