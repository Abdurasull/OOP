from colorama import Fore, Style, Back
#  Movie Class (Film):

# Movie nomli class yarating, quyidagi atributlarga ega:
# title (nomi),
# duration (davomiyligi, minutda),
# rating (reyting).
# Quyidagi metodlarni qo‘shing:
# increase_duration(minutes) — filmning davomiyligini minutes minutga oshirsin.
# Agar davomiylik 150 minutdan oshsa, reytingni 0.5 ga kamaytiruvchi metod yozing.

class Movie:
    def __init__(self, title: str, duration: int, rating: int):
        self.title = title
        self.duration = duration
        self.rating = rating
    def increase_duration(self):
        if self.duration > 150:
            self.rating -= 0.5
        

movie1 = Movie("O`g`rinig muhabbati", 160, 3)
movie2 = Movie("Kichkina tabib", 120, 5.5)


movie1.increase_duration()
movie2.increase_duration()
print(movie1.rating)
print(movie2.rating)