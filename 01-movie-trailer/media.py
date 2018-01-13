import requests

# Global config
# In case the api key is no longer valid or expired, request a new key from https://developers.themoviedb.org/3
api_key = "deaf4801db900d3210957270a85fe43c"

class Movie():
    def __init__(self):
        self.id = None
        self.title = None
        self.poster_image_url = None
        self.overview = None
        self.release_date = None
        self.original_language = None
        self.trailer_youtube_url = None

def query_movies_data():
    # Get all popular movies from TMDb
    print("Download basic information of popular movies...")
    discover_url = f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key={api_key}&/discover/movie?sort_by=popularity.desc"
    data = requests.get(discover_url).json()
    movies = []

    # Iterate all popular movies from results
    for movie_data in data["results"]:
        # Create movie object
        movie = Movie()
        movie.id = movie_data["id"]
        movie.title = movie_data["title"]
        movie.poster_image_url = "https://image.tmdb.org/t/p/w500" + movie_data["poster_path"]
        movie.overview = movie_data["overview"]
        movie.release_date = movie_data["release_date"]
        movie.original_language = movie_data["original_language"]

        # Make another api call to retrieve youtube trailer url
        print(f"Download youtube trailer link for '{movie.title}'...")
        video_url = f"https://api.themoviedb.org/3/movie/{movie.id}/videos?api_key={api_key}"
        video_data = requests.get(video_url).json()["results"]

        if len(video_data) > 0:
            youtube_key = video_data[0]["key"]
            movie.trailer_youtube_url = f"https://www.youtube.com/watch?v={youtube_key}"

        # Add movie object into final list
        movies.append(movie)

    return movies
