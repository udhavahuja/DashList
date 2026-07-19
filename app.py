#Required imports
from flask import Flask, session, jsonify, redirect
from flask_session import Session

#KEYS AND Decorators
from config.config import SECRET_SESSION_KEY
from utils.decorators import login_required
from config.database import get_db

#importing blueprints
from routes.auth_routes import auth_bp
from routes.browse_routes import browse_bp
from routes.library_routes import library_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)

with get_db as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")

    if cursor.fetchone() is None:
        with open("schema.sql", "r") as f:
            conn.executescript(f.read())

app.secret_key = SECRET_SESSION_KEY
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PEREMENENT"] = False
Session(app)

#Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(browse_bp)
app.register_blueprint(library_bp)
app.register_blueprint(dashboard_bp)

@app.route("/")
@login_required
def index():
    return redirect("/dashboard")

@app.route("/test")
def test():
    return jsonify({"user_id": session.get("user_id")})

if __name__ == '__main__':
    app.run()