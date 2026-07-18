from dotenv import load_dotenv
import os

load_dotenv()

SECRET_SESSION_KEY = os.getenv("SECRET_SESSION_KEY")

#TMDB
TMDB_API_KEY = os.getenv("TMDB_API")
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMG_URL = "https://image.tmdb.org/t/p/w500"

#Google books
GBOOKS_API_KEY = os.getenv("BOOKS_API")
GBOOKS_BASE_URL = "https://www.googleapis.com/books/v1/volumes"