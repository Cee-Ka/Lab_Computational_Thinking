class Movie:
    def __init__(self, title, director, price):
        self.title, self.director, self.price = title, director, price
        self.is_rented = False


class Rental:
    def __init__(self):
        self.movies = []
        self.income = 0

    def add_movie(self, movie):
        self.movies.append(movie)

    def rent_movie(self, title):
        for m in self.movies:
            if m.title == title and not m.is_rented:
                m.is_rented = True
                self.income += m.price
                print(f"{m.title} rented")
                return
        print("Cannot rent.")

    def return_movie(self, title):
        for m in self.movies:
            if m.title == title and m.is_rented:
                m.is_rented = False
                print(f"Returned: {m.title}")
                return
        print("Cannot return.")

    def get_rented_movies(self):
        rented = [m.title for m in self.movies if m.is_rented]
        print("Renting list:", rented or "None")

    def get_total_income(self):
        print(f"Total income: {self.income:,}₫")

rental = Rental()
rental.add_movie(Movie("Inception", "Nolan", 30000))
rental.add_movie(Movie("Avatar", "Cameron", 40000))
rental.add_movie(Movie("Titanic", "Cameron", 25000))

rental.rent_movie("Inception")
rental.rent_movie("Avatar")
rental.get_rented_movies()
rental.return_movie("Inception")
rental.get_total_income()
