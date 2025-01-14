from colorama import Fore, Style, Back
# Student class yarating. Har bir talabaning ism-familiyasi, kursi va o'rtacha bahosi bo'lsin. 
# Talabaning to'liq ismini chiqaruvchi metod yozing.


class Student:
    def __init__(self, lastname: str, firstname: str, cours: int, grade: float):
        self.lasname = lastname
        self.firstname = firstname
        self.cours = cours
        self.grade = grade

    def fullname(self):
        return f"{Fore.RED}my name is{Fore.RESET} {Fore.YELLOW}{self.lasname} {self.firstname}{Fore.RESET}"


lastname = input(f"{Fore.BLUE}familiyangizni kiriting: {Fore.RESET}")
firstname = input(f"{Fore.BLUE}Ismingizni kiriting: {Fore.RESET}")
while True:
    try:
        kurs = int(input(f"{Fore.BLUE}Kursingizni kiriting: {Fore.RESET}"))
        break
    except:
        print(f"{Fore.RED}Iltimos faqat butun son kiriting!{Fore.RESET}\n")

while True:
    try:
        baha = float(input(f"{Fore.BLUE}O`rtacha bahoni kiriting: {Fore.RESET}"))
        break
    except:
        print(f"{Fore.RED}Iltimos faqat butun  yoki float son kiriting!{Fore.RESET}\n")

student1 = Student(lastname, firstname, kurs, baha)

print(student1.fullname())