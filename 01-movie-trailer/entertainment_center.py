from media import query_movies_data
from fresh_tomatoes import open_movies_page

movies = query_movies_data()
open_movies_page(movies)

# for movie in movies:
#     print()
#     print(movie.id)
#     print(movie.title)          
#     print(movie.poster_image_url)
#     print(movie.overview)
#     print(movie.release_date)
#     print(movie.original_language)
#     print(movie.trailer_youtube_url)
#     print()




# fresh_tomatoes.open_movies_page(movies)