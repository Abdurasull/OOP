from datetime import datetime

hozzirgi_vaqt = datetime.now()
time_result = hozzirgi_vaqt.strftime("%Y-%m-%d  %H:%M:%S")

def add_file(student_name: str):
    with open("add_file.txt", "a") as file:
        file.write(f"{time_result} da yangi talaba qo`shildi: \n{student_name}\n\n")