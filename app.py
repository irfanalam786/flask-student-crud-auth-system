
from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secretkey"
DATABASE = "database.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db()
    db.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    db.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        course TEXT
    )
    """)
    db.commit()

init_db()

@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        db = get_db()
        try:
            db.execute("INSERT INTO users(username,password) VALUES(?,?)",(username,password))
            db.commit()
        except:
            return "User already exists"
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username=?",(username,)).fetchone()
        if user and check_password_hash(user["password"], password):
            session["user"] = username
            return redirect("/dashboard")
        return "Invalid username or password"
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

@app.route("/students")
def students():
    if "user" not in session:
        return redirect("/login")
    db = get_db()
    data = db.execute("SELECT * FROM students").fetchall()
    return render_template("students.html", students=data)

@app.route("/add-student", methods=["GET","POST"])
def add_student():
    if "user" not in session:
        return redirect("/login")
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]
        db = get_db()
        db.execute("INSERT INTO students(name,email,course) VALUES(?,?,?)",(name,email,course))
        db.commit()
        return redirect("/students")
    return render_template("add_student.html")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit_student(id):
    if "user" not in session:
        return redirect("/login")
    db = get_db()
    student = db.execute("SELECT * FROM students WHERE id=?",(id,)).fetchone()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]
        db.execute("UPDATE students SET name=?,email=?,course=? WHERE id=?",(name,email,course,id))
        db.commit()
        return redirect("/students")
    return render_template("edit_student.html", student=student)

@app.route("/delete/<int:id>")
def delete_student(id):
    if "user" not in session:
        return redirect("/login")
    db = get_db()
    db.execute("DELETE FROM students WHERE id=?",(id,))
    db.commit()
    return redirect("/students")

if __name__ == "__main__":
    app.run(debug=True)
