# Django Backend Project

A robust Django REST API boilerplate featuring JWT Authentication, CORS support, and the Jazzmin admin dashboard.

## 1. Directory Structure
```text
backend/
├── manage.py
├── backend/
│   ├── settings.py
│   └── urls.py
├── myapp/
└── venv/
```


## 2. Create directory and virtual environment
mkdir backend
cd backend
python -m venv venv

# Activate Environment
# Windows:
cd venv\Scripts\activate
- then do `activate.bat`  
# Mac/Linux:
source venv/bin/activate

# Install Dependencies
pip install django djangorestframework django-jazzmin django-cors-headers djangorestframework-simplejwt



# Start Project and App
django-admin startproject myproject .
python manage.py startapp myapp
