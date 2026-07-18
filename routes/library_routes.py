from flask import Blueprint, request, redirect, session, render_template

from utils.decorators import login_required
from services.library_service import add_library, get_library, make_editable, edit_library, delete_library

library_bp = Blueprint("library_bp", __name__)

@library_bp.route("/library/add", methods = ["POST"])
@login_required
def add():
    user_id = session.get("user_id")
    source = request.form.get("source")
    api_id = request.form.get("api_id")
    title = request.form.get("title")
    media_type = request.form.get("media_type")
    description = request.form.get("description")
    release_year = request.form.get("release_year")
    cover_url = request.form.get("cover_url")
    authors = request.form.get("authors") or None

    add_library(source, api_id, title, media_type, description, release_year, cover_url, authors, user_id)

    return redirect("/library")

@library_bp.route("/library")
@login_required
def lib():
    user_id = session.get("user_id")
    library_items = get_library(user_id)

    return render_template("library/library.html", library_items=library_items)

@library_bp.route("/library/edit", methods = ["GET", "POST"])
@login_required
def edit():
    if request.method == "GET":
        user_id = session.get("user_id")
        source = request.args.get("source")
        api_id = request.args.get("api_id")

        item = make_editable(user_id=user_id, api_id=api_id, source=source)

        return render_template("library/edit-library.html", item = item)
    
    if request.method == "POST":
        user_id = session.get("user_id")
        api_id = request.form.get("api_id")
        source = request.form.get("source")
        status = request.form.get("status")
        rating = request.form.get("rating")

        edit_library(user_id=user_id, api_id=api_id, source=source, status=status, rating=rating)

        return redirect("/library")
        
@library_bp.route("/library/delete", methods=["POST"])
@login_required
def delete_entry():
    user_id = session.get("user_id")
    api_id = request.form.get("api_id")
    source = request.form.get("source")

    delete_library(user_id, api_id, source)

    return redirect("/library")
