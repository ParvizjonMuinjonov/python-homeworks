import requests
from dotenv import load_dotenv
import os
import random

load_dotenv()

api_key = os.getenv("API_KEY2")
BASE_URL = "https://api.themoviedb.org/3"
url = f"{BASE_URL}/genre/movie/list?api_key={api_key}&language=en-US"
response = requests.get(url)
genres = response.json()

user_genre = input("Enter a genre: ").strip().title()

genre_id = None
for genre in genres["genres"]:
    if genre["name"] == user_genre:
        genre_id = genre["id"]
        break

if not genre_id:
    print("Invalid genre")
    exit()


url = f"{BASE_URL}/discover/movie?api_key={api_key}&with_genres={genre_id}&language=en-US&page=1"
response = requests.get(url)
movies = response.json()["results"]


if movies:
    random_movie = random.choice(movies)
    print(f"🎬 Recommended Movie: {random_movie['title']}")
    print(f"📆 Release Date: {random_movie['release_date']}")
    print(f"⭐ Rating: {random_movie['vote_average']}")
    print(f"📖 Overview: {random_movie['overview']}")
else:
    print("No movies found in this genre. Try another.")
