from colorama import Fore, Style, Back
import os
from menu import menu
from add_base import add_file
class Maktab:
    def __init__(self, maktab_nomi: str):
        self.name = maktab_nomi
        self.talabalar = [] 
    
    # talabalarni qo`shish uchun function
    def add_student(self, student_name: str):
        if student_name not in self.talabalar:
            self.talabalar.append(student_name)
            print(f"{Fore.YELLOW}{student_name}{Fore.BLUE} nomli talaba mufoffaqiyatli ruyxatga olindi{Fore.RESET}\n")
            add_file(student_name)
        else:
            print(f"{Fore.BLUE}Bunday nomli talaba, allaqachon ruyxatda mavjud{Fore.RESET}\n")
    # talabalar ruyxatini chiqarish
    def ruyxat(self):
        if self.talabalar:
            for talaba in range(len(self.talabalar)):
                print(f"{Fore.YELLOW}{talaba + 1} - talaba: {self.talabalar[talaba]}{Fore.RESET}")
    # Talabalarni ruyxatdan o`chirish
    def pop_students(self, student):
        if student in self.talabalar:
            self.talabalar.remove(student)
        else:
            print(f"{Fore.RED}Bunday talaba ruyxatga olinmagan, iltimos tikshirib qaytadan kiriting\n")

# dasturimiz ishga tushganda bungacha bulgan barcha yozilganlarni terminaldan o`chirish uchun ishlatiladi
os.system('clear')

# maktabga nom berib olamiz
print(f"{Fore.YELLOW}Assalomu alaykum, dasturimizga hush kelebsiz!\n{Fore.RESET}")
name_school = input("Maktabimizga nom tanlang: ")
maktab = Maktab(name_school)

while True:
    menu()
    x = input("Buyruqni kiriting: ")
    if x == '1':
        name = input(f"{Fore.LIGHTBLACK_EX}Talabani ismini kiriting: ")
        maktab.add_student(name)
        
    elif x == '2':
        name = input(f"{Fore.LIGHTBLACK_EX}Talabani ismini kiriting: ")
        maktab.pop_students(name)
        
    elif x == '3':
        print(f"{Fore.GREEN}Maktabimiz talamalari:")
        maktab.ruyxat()
    elif x == '0':
        print(f"{Fore.GREEN}Buncha tiz ketyabsiz😳{Fore.RESET}")
        exit()
    else:
        print(f"{Fore.RED}Siz noto`g`ri buyruq kiritdingiz, iltimos tikshirib qaytadan kiriting!{Fore.RESET}\n")
