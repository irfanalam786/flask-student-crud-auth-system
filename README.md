# Flask Authentication & CRUD Student Management System

## Project Overview

This project is a **Flask-based web application** that implements a secure **User Authentication System** along with a **Database-Driven CRUD module**.

The application allows registered users to log in and manage student records through a simple dashboard interface.

This project was developed as part of the **Python Full Stack Web Development Internship (Task-3)**.

---

# Features

### User Authentication

* User Registration
* Secure Password Hashing
* User Login System
* Session-Based Authentication
* Logout Functionality

### CRUD Operations

* Add Student
* View Student Records
* Edit Student Details
* Delete Student Records

### Security Features

* Passwords stored using hashing
* Protected routes using Flask sessions
* Unauthorized users redirected to login

---

# Technology Stack

Backend:

* Python
* Flask

Frontend:

* HTML
* CSS

Database:

* SQLite

Security:

* Flask Sessions
* Werkzeug Password Hashing

---

# Project Structure

```
flask-student-crud-auth-system/

app.py
database.db

templates/
    login.html
    register.html
    dashboard.html
    add_student.html
    students.html
    edit_student.html

static/
    style.css
```

---

# Installation & Setup

### 1 Install Dependencies

```
pip install flask werkzeug
```

### 2 Run Application

```
python app.py
```

### 3 Open Browser

```
http://127.0.0.1:5000
```

---

# Authentication Workflow

1. User registers an account
2. Password is securely hashed before storing
3. User logs in using credentials
4. Session is created for authenticated user
5. Protected routes allow CRUD operations
6. Logout clears the user session

---

# Learning Outcomes

* Understanding Flask routing and templates
* Implementing authentication systems
* Connecting Flask with SQLite database
* Building CRUD applications
* Managing session-based security

---

# Author

**Irfan Alam**
Python Full Stack Developer (Learner)

GitHub
https://github.com/irfanalam786

LinkedIn
https://www.linkedin.com/in/irfan-alam-786t
