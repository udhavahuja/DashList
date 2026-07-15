from datetime import datetime

from config.database import get_db

#update library database (Returns nothing)
def add_library(source, api_id, title, media_type, description, release_year, cover_url, authors, user_id):
    conn= get_db()
    cursor=  conn.cursor()

    check = cursor.execute("SELECT * FROM media WHERE api_id = ? AND source = ?", (api_id, source))

    if not check.fetchone():
        cursor.execute("""INSERT INTO media
                        (source, api_id, title, type, description, release_year, cover_url, authors)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                        (source, api_id, title, media_type, description, release_year, cover_url, authors)
                      )
        conn.commit()

    media_id = cursor.execute("SELECT id FROM media WHERE api_id = ? AND source = ?", (api_id, source)).fetchone()["id"]

    check = cursor.execute("SELECT * FROM entries WHERE user_id = ? AND media_id = ?", (user_id, media_id))
    if check.fetchone():
        return "Already Added"
    
    cursor.execute("""INSERT INTO entries
                    (user_id, media_id, status, added_at)
                    VALUES (?, ?, ?, ?)""",
                    (user_id, media_id, "Planned", datetime.now())
                  )
    conn.commit()

    cursor.close()
    conn.close()

#Fetch content for library
def get_library(user_id):
    conn = get_db()
    cursor= conn.cursor()

    library_items=[]
    rows= cursor.execute("""SELECT media.api_id, media.source, title, cover_url, description, type, authors, release_year, status, rating, added_at
                         FROM entries 
                         JOIN media 
                         ON entries.media_id = media.id
                         WHERE user_id = ?""", (user_id,)).fetchall()
    
    for entry in rows:
        library_items.append(entry)

    cursor.close()
    conn.close()

    return library_items

def make_editable(user_id, api_id, source):
    conn = get_db()
    cursor= conn.cursor()

    media_id = cursor.execute("SELECT id FROM media WHERE api_id = ? AND source = ?", (api_id, source)).fetchone()["id"]


    row= cursor.execute("""SELECT media.api_id, media.source, media.title, media.cover_url, media.description, media.type, media.authors, media.release_year, entries.status, entries.rating, entries.added_at
                         FROM entries 
                         JOIN media 
                         ON entries.media_id = media.id
                         WHERE entries.user_id = ?
                         AND entries.media_id = ?""", (user_id, media_id)).fetchone()

    cursor.close()
    conn.close()

    return row

#Edit library card
def edit_library(user_id, api_id, source, status, rating):
    conn = get_db()
    cursor= conn.cursor()
    
    media_id = cursor.execute("SELECT id FROM media WHERE api_id = ? AND source = ?", (api_id, source)).fetchone()["id"]
    entry_id = cursor.execute("SELECT id FROM entries WHERE user_id = ? AND media_id = ?", (user_id, media_id)).fetchone()["id"]

    cursor.execute("UPDATE entries SET status = ?, rating = ? WHERE id = ?", (status, rating, entry_id))
    conn.commit()

    cursor.close()
    conn.close()

#Delete library card
def delete_library(user_id, api_id, source):
    conn = get_db()
    cursor = conn.cursor()

    media_id = cursor.execute("SELECT id FROM media WHERE api_id = ? AND source = ?", (api_id, source)).fetchone()["id"]
    entry_id = cursor.execute("SELECT id FROM entries WHERE user_id = ? AND media_id = ?", (user_id, media_id)).fetchone()["id"]

    cursor.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
    conn.commit()

    cursor.close()
    conn.close()