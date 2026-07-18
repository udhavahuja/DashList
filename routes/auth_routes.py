from flask import Blueprint, request, render_template, session, redirect, flash
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
            flash("All fields required","danger")
            return redirect("/register")
        
        users = cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        if users.fetchone() is not None:
            flash("User already registered","warning")
            return redirect("/login")
        
        if password != confirmation:
            flash("Passwords don't match","danger")
            return redirect("/register")

        hashed_password = generate_password_hash(password)

        user = create_user(username = username, pass_hash = hashed_password, email = email)

        cursor.execute("INSERT INTO users (username, email, password_hash, created_at) VALUES (?, ?, ?, ?)", (user["username"], user["email"], user["password_hash"], user["created_at"]))
        conn.commit()

        #session to be created

        cursor.close()
        conn.close()

        flash("Account created. Please log-in", "success")
        return redirect("/login")
    
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
            flash("All fields required","danger")
            return redirect("/login")
        
        rows = cursor.execute("SELECT * FROM users WHERE email = ?", (mail,))
        user = rows.fetchone()

        if user is None:
            flash("Invalid Email/Password","danger")
            return redirect("/login")
        
        if not check_password_hash(user["password_hash"], password):
            flash("Invalid Email/Password","danger")
            return redirect("/login")
        
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