from media import query_movies_data
from fresh_tomatoes import open_movies_page

if __name__ == "__main__":
    popular_movies = query_movies_data()
    open_movies_page(popular_movies)