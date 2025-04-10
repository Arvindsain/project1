# README.md

## Django Based Q&A Platform

A simple Quora-inspired Q&A website built using Django. This project includes functionality for users to register, login, post questions, answer questions, and like answers.

---

## 🚀 Features

- User registration & login/logout
- Ask and view questions
- Answer other users' questions
- Like answers

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Arvindsain/project1.git
cd project1
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirement.txt
```

### 3. Apply Migrations
```bash
cd project
python manage.py migrate
```

### 4. Create Superuser (optional)
```bash
python manage.py createsuperuser
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/`

---
