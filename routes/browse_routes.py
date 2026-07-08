from flask import Blueprint, request, render_template

from services.browse_service import search_books, search_media

browse_bp = Blueprint("browse_bp", __name__)

@browse_bp.route("/browse", methods = ["GET"])
def browse():
    query = request.args.get('query')
    if query is None:
        return render_template("browse/browse.html")

    media_type = request.args.get('media_type')

    if media_type == 'book':
        books = search_books(query=query)
        print(books)
        print(type(books))
        return render_template('browse/browse.html', books=books, media_type=media_type)
    else:
        media_list= search_media(query=query, media_type=media_type)
        return render_template('browse/browse.html', media_list=media_list, media_type=media_type)