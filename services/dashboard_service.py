from flask import jsonify
from config.database import get_db

def dash_content(user_id):
    conn = get_db()
    cursor = conn.cursor()

    name = cursor.execute("SELECT username FROM users where id = ?", (user_id,)).fetchone()["username"]
    total_media = cursor.execute("SELECT COUNT(*) AS total_media FROM entries where user_id = ?", (user_id,)).fetchone()["total_media"]
    movies = cursor.execute("SELECT COUNT(*) AS movies FROM entries JOIN media ON media.id = entries.media_id WHERE media.type = 'movie' and user_id = ?", (user_id,)).fetchone()["movies"]
    tv = cursor.execute("SELECT COUNT(*) AS tv FROM entries JOIN media ON media.id = entries.media_id WHERE media.type = 'tv' and user_id = ?", (user_id,)).fetchone()["tv"]
    books = cursor.execute("SELECT COUNT(*) AS books FROM entries JOIN media ON media.id = entries.media_id WHERE media.type = 'book' and user_id = ?", (user_id,)).fetchone()["books"]
    completed = cursor.execute("SELECT COUNT(*) AS completed FROM entries WHERE status = 'completed' and user_id = ?", (user_id,)).fetchone()["completed"]
    ongoing = cursor.execute("SELECT COUNT(*) AS ongoing FROM entries WHERE status = 'ongoing' and user_id = ?", (user_id,)).fetchone()["ongoing"]

    dash = {
        "name" : name,
        "total_media" : total_media,
        "movies" : movies,
        "tv" : tv,
        "books" : books,
        "completed" : completed,
        "ongoing" : ongoing
    }

    cursor.close()
    conn.close()

    return dash