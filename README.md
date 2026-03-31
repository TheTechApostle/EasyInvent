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

### Windows:
```
    - cd venv\Scripts\activate
    - then do `activate.bat`  
    - python manage.py startapp myapp
```
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









