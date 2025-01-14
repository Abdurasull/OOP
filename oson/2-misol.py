from colorama import Fore, Style, Back
# Employee class yarating. Har bir xodimning ismi va oylik maoshi bo'lsin. 
# Xodimning yillik maoshini hisoblovchi metod yozing.
class Employee:
    def __init__(self, name: str, salary: float):
      self.name = name
      self.salary = salary

    def annual_salary(self)->str:
       return f"{Fore.CYAN}{self.name} ning 1 yillig maoshining qiymati:{Fore.RESET}{Fore.YELLOW} {float(self.salary)*12}{Fore.RESET}"
    

name = input(f"{Fore.CYAN}Ismingizni kiriting: {Fore.RESET}")
salary = input(f"{Fore.CYAN}1-oylik ish haqqini kiriting: {Fore.RESET}")

employee = Employee(name, salary)

print(employee.annual_salary())
