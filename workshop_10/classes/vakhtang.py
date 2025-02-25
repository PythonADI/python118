class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

    def display_info(self):
        print(f"title {self.title}")
        print(f"year {self.year}")
        print(f"genre {self.genre}")


movie = Movie("avengers", 2017, "fantasy")
movie.display_info()
print("______________________")
print(movie.display_info())
