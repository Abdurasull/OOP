from colorama import Fore, Style, Back


class Dukon:
    def __init__(self, name: str, addres: str, Maxsulot: str, time_work: int):
        self.name = name
        self.addres = addres
        self.Maxsulot = Maxsulot
        self.time_work = time_work
    def sort(self):
        if self.Maxsulot == "elektro":
            print(f"{Fore.CYAN}Dukon nomi: {Fore.YELLOW}{self.name}{Fore.CYAN}\nDukon manzili: {Fore.YELLOW}{self.addres}\n{Fore.CYAN}Maxsulot turi: {Fore.YELLOW}{self.Maxsulot}\n{Fore.CYAN}Ish davomiyligi: {Fore.YELLOW}{self.time_work}{Fore.RESET}\n")

dukon1 = Dukon("Maxmut bobo", 'Samarqand gagarin 157', "elektro", 12)
dukon2 = Dukon("Market_go", 'Urgut_sity', "oziq-ovqat", 9)
dukon3 = Dukon("lampa_uz", 'Samarqand registon', "elektro", 8)
dukon4 = Dukon("Xoz_maxsulot", 'daxbit 145', "Hoz tavar", 24)
dukon5 = Dukon("Multi", 'Samarqand silisky', "elektro", 12)

dukon1.sort()
dukon2.sort()
dukon3.sort()
dukon4.sort()
dukon5.sort()


