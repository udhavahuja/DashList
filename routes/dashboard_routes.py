from flask import Blueprint, session, render_template

from services.dashboard_service import dash_content

dashboard_bp = Blueprint("dashboard_bp", __name__)

@dashboard_bp.route("/dashboard", methods = ["GET"])
def dashboard():
    user_id = session.get("user_id")

    content = dash_content(user_id)

    return render_template("dashboard/dashboard.html", content = content)