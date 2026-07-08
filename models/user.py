from datetime import datetime

def create_user(username, email, pass_hash):
    return {
        "username" : username,
        "email" : email,
        "password_hash" : pass_hash,
        "created_at" : datetime.now().isoformat()
    }