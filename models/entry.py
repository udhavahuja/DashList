from datetime import datetime

def creat_entry(user_id, media_id, status, rating = None, review = None):
    return {
        "user_id" : user_id,
        "media_id" : media_id,
        "status" : status,
        "rating" : rating,
        "review" : review,
        "added_at" : datetime.now().isoformat(),
        "updated_at" : datetime.now().isoformat()
    }