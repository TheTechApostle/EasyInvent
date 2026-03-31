# Django Backend Project

A robust Django REST API boilerplate featuring JWT Authentication, CORS support, and the Jazzmin admin dashboard.

# Create Repository
``` - mkdir  easyinvent
    - cd easyinvent

```
# Start Project and App
```
 - django-admin startproject backend
 - cd backend
```

# Create virtual environment
```
- python -m venv venv
```

# Activate Environment

# 1. Activate the environment
# Make sure you are in the \backend\ folder
cd into venv\Scripts\ 
then run **activate.bat**

# 2. Create your app
python manage.py startapp myapp

# 3. Run the server to test
python manage.py runserver

### Mac/Linux:
```
source venv/bin/activate
```

# Install Dependencies
`pip install django djangorestframework django-jazzmin django-cors-headers djangorestframework-simplejwt`



## . Directory Structure
```text
backend/
├── manage.py
├── backend/
│   ├── settings.py
│   └── urls.py
├── myapp/
└── venv/
```









