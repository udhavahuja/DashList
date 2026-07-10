from flask import Blueprint, request, redirect, session, render_template

from config.database import get_db
from services.library_service import add_library, get_library

library_bp = Blueprint("library_bp", __name__)

@library_bp.route("/library/add", methods = ["POST"])
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
def lib():
    user_id = session.get("user_id")
    library_items = get_library(user_id)

    return render_template("library/library.html", library_items=library_items)