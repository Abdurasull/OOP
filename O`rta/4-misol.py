from colorama import Fore, Style, Back
from datetime import datetime
#  Talaba (Student) class yarating.
# Elementlari:

# Talaba ismi;
# O‘qish kursi;
# O‘rtacha bahosi;
# Stipendiya miqdori.
# Shart:

# 5 ta obyekt yarating.
# O‘rtacha bahosi 80 dan yuqori va stipendiya miqdori 1 mln so‘mdan katta bo‘lgan talabalar haqida ma’lumot chiqaring.

class Student:
    def __init__(self, name: str, cours: int, urtacha_baho: int, stipendiya: int)->None:
        self.name = name
        self.course = cours
        self.urtacha_baho = urtacha_baho
        self.stipendiya = stipendiya

    def sort(self):
        if self.urtacha_baho > 80 and self.stipendiya > 1_000_000:
            print(f"""
Talabaning ismi: {self.name}
Talabaning kursi: {self.course}
Talabaning kursi: {self.urtacha_baho}
                    """)


Student_list = []
Student_list.append(Student("Abdurasul", 2, 79, 1_200_000))
Student_list.append(Student("Bobur", 1, 70, 800_000))
Student_list.append(Student("Anora", 4, 90, 1_500_000))
Student_list.append(Student("Azizbek", 1, 60, 600_000))
Student_list.append(Student("Bunyod", 4, 95, 1_300_000))

for student in Student_list:
    student.sort()
