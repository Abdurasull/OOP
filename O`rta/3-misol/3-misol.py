from colorama import Fore, Style, Back
from datetime import datetime
# Student (talaba):

# Student classini yarating, atribut sifatida ism (name), yosh (age), va baholar (grades) ro‘yxatini qabul qilsin.
# get_average methodini yozing, bu method talabaning o‘rtacha bahosini qaytarsin.
# is_passing methodi esa o‘rtacha baho 60 dan yuqori bo‘lsa True, aks holda False qaytarsin.

class Student:
    grades = []
    def __init__(self, name: str, age: int,)->None:
        self.name = name
        self.age = age

    def add_ball(self, science_ball: int):
        self.grades.append(science_ball)

    def get_average(self)->float:
        self.urtacha = sum(self.grades)/len(self.grades)
        return self.urtacha
    
    def is_passing(self):
        if self.get_average() > 60:
            return 'true'
        else:
            return 'false'

# Talabani yoshini va ishmini kiritamiz
Student1 = Student("Abdurasul", 27)

# talabaga ball beramiz
Student1.add_ball(60)
Student1.add_ball(76)
Student1.add_ball(80)

# Talabani o`rtacha balini hisoblaymiz
urtacha_ball = Student1.get_average()
print(f"{Fore.CYAN}{Student1.name}ning o`rtacha ball:{Fore.RESET} {Fore.YELLOW}{urtacha_ball} {Fore.CYAN}va buning qiymati: {Fore.RESET}{Fore.YELLOW}{Student1.is_passing()}{Fore.RESET}")




        