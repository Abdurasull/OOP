from colorama import Fore, Style, Back

#menu ni doim yozmazlik uchun uni alohida functionga yaratib olaman
def menu():
    print(f"{Fore.CYAN}Dasturdan foydalanish buyruqlari:\n{Fore.BLUE}Ruyxatga talaba qo`shish uchun: {Fore.YELLOW}1\n{Fore.BLUE}Ruyxatdan talaba o`chirish uchun: {Fore.YELLOW}2\n{Fore.BLUE}Ruyxatni ko`rish uchun: {Fore.YELLOW}3\n{Fore.BLUE}Dasturdan chiqish uchun: {Fore.YELLOW}0{Fore.RESET}")
