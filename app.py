#Required imports
from flask import Flask, session, jsonify, render_template
from flask_session import Session

#KEYS AND Decorators
from config.config import SECRET_SESSION_KEY
from utils.decorators import login_required

#importing blueprints
from routes.auth_routes import auth_bp

app = Flask(__name__)

app.secret_key = SECRET_SESSION_KEY
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PEREMENENT"] = False
Session(app)

#Register blueprints
app.register_blueprint(auth_bp)

@app.route("/")
@login_required
def index():
    return render_template("dashboard/dashboard.html")

@app.route("/test")
def test():
    return jsonify({"user_id": session.get("user_id")})

if __name__ == '__main__':
    app.run()