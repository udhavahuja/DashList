from flask import Blueprint, request, jsonify, render_template, session, redirect
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

from config.database import get_db
from models.user import create_user

auth_bp = Blueprint("auth_bp", __name__)

#Register
@auth_bp.route("/register", methods = ["POST", "GET"])
def register():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not email or not password or not confirmation:
            return jsonify({"error" : "All fields required"}), 400
        
        users = cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        if users.fetchone() is not None:
            return jsonify({"error" : "User already registered"}), 409
        
        if password != confirmation:
            return jsonify({"error" : "Password don't match"}), 400

        hashed_password = generate_password_hash(password)

        user = create_user(username = username, pass_hash = hashed_password, email = email)

        cursor.execute("INSERT INTO users (username, email, password_hash, created_at) VALUES (?, ?, ?, ?)", (user["username"], user["email"], user["password_hash"], user["created_at"]))
        conn.commit()

        #session to be created

        cursor.close()
        conn.close()

        return redirect("/")
    
    else:
        return render_template("auth/register.html")
    
#login
@auth_bp.route("/login", methods = ["POST", "GET"])
def login():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":
        mail = request.form.get("email")
        password = request.form.get("password")
        if not mail or not password:
            return jsonify({"error" : "All fields required"}), 400
        
        rows = cursor.execute("SELECT * FROM users WHERE email = ?", (mail,))
        user = rows.fetchone()

        if user is None:
            return jsonify({"error" : "Invalid Username/Password"}), 400
        
        if not check_password_hash(user["password_hash"], password):
            return jsonify({"error" : "Invalid Username/Password"}), 400
        
        session["user_id"] = user["id"]

        cursor.close()
        conn.close()
        
        return redirect("/")
    
    else:
        return render_template("auth/login.html")
    
#logout
@auth_bp.route("/logout", methods = ["POST"])
def logout():
    session.clear()
    return redirect("/login")