def create_media(source, api_id, title, media_type, description, release_year, cover_url):
    return {
        "source" : source,
        "api_id" : api_id,
        "title" : title,
        "mtype" : media_type,
        "description" : description,
        "release_year" : release_year,
        "cover_url" : cover_url
    }

def create_book(api_id, title, authors, cover_url, release_year, description):
    return {
        "source" : "Google Books",
        "api_id" : api_id,
        "title" : title,
        "authors" : authors,
        "description" : description,
        "release_year" : release_year,
        "cover_url" : cover_url
    }