#Required Imports
from flask import jsonify
import requests
from models.media import create_media, create_book
#Keys
from config.config import TMDB_API_KEY, TMDB_BASE_URL, TMDB_IMG_URL, GBOOKS_BASE_URL, GBOOKS_API_KEY

#Searching for movies or tv shows
def search_media(query, media_type):
    url = f"{TMDB_BASE_URL}/search/{media_type}"
    params = {"api_key": TMDB_API_KEY, "query": query,}

    response = requests.get(url, params=params)

    #Checking for errors
    if response.status_code == 200:
        data = response.json()
    else:
        return jsonify({"error" : f"Code : {response.status_code}"})
    
    media_list=[]
    
    for content in data["results"]:

        #Check if poster url is none
        if content["poster_path"]:
            cover= TMDB_IMG_URL + content.get("poster_path")
        else:
            cover = None

        #Classifying tv and movie
        if media_type == 'tv':
            title = content['name']
            date = content['first_air_date']
        else:
            title = content['title']
            date = content["release_date"]

        #Checking if date is null
        if date:
            release_year = int(date[0:4])
        else:
            release_year = None

        #Creating media
        media = create_media(
            source="TMDB",
            api_id= content["id"],
            title= title,
            media_type= media_type,
            description= content.get("overview", ""),
            release_year= release_year,
            cover_url= cover
            )
        
        media_list.append(media)

    return media_list


#Searching Books
def search_books(query):
    url = GBOOKS_BASE_URL
    params = {"key": GBOOKS_API_KEY, "q": query}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
    else:
        return [{"error" : f"Code : {response.status_code}"}]

    books=[]

    for item in data.get("items", []):
        info = item.get("volumeInfo", {})

        books.append(
            create_book(
                api_id= item["id"],
                title= info.get("title"),
                authors= ", ".join(info.get("authors", [])),
                description=info.get("description"),
                year= info.get("publishedDate", "")[:4],
                cover_url= info.get("imageLinks", {}).get("thumbnail")
            )
        )

    return books