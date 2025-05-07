
# 🎓CAMPUS EVENT MANAGEMENT SYSTEM (Admin Backend)

A Django-powered backend platform that streamlines campus event coordination by enabling admins to manage users, events, certificates, and notices—all from a centralized dashboard. Designed for efficient campus operations and easy access to academic and extracurricular records.

---

## 📽️ Demo Video
[Watch Demo](event management system mini.mp4)

## 📄 Project Report pdf
[View Project Report (PDF)](college event management report.docx)

## 📊 Presentation Slides
[View Presentation (PDF)](MINI_PROJECT_PRESENTATION[1].pdf)

---

## ✅ Features

- Admin login with secure access
- Role-based control for admin staff
- Upload and manage event notices
- Generate and store student certificates
- Add/edit/delete upcoming events
- Simple dashboard to monitor all backend data

---

## 🛠️ Tech Stack

- **Backend Framework**: Django (Python)
- **Database**: SQLite3 (default Django DB)
- **Admin Interface**: Django Admin Panel
- **Server**: Django Development Server (`manage.py runserver`)
- **Language**: Python 3.x
- **Authentication**: Django built-in user auth with admin/staff support

---
## 🗂 Project Structure ``` campus_event_manager_backend/ │ ├── campus_event/ # Main Django project folder │ ├── __init__.py │ ├── settings.py # Project configuration and settings │ ├── urls.py # URL routing for the entire project │ ├── asgi.py │ └── wsgi.py │ ├── event_management/ # Django app for events, certificates, notices │ ├── migrations/ # Database migration files │ │ └── __init__.py │ ├── __init__.py │ ├── admin.py # Admin panel setup for all models │ ├── apps.py │ ├── models.py # Models: Event, Notice, Certificate │ ├── tests.py │ └── views.py # App views (if any) │ ├── db.sqlite3 # Default SQLite database ├── manage.py # Django project manager script └── requirements.txt # Python dependencies ``` </pre>
---

## 🧑‍💻 Local Setup Guide

Follow these steps to run the project locally:

1. **Clone the repository**
  
   git clone https://github.com/your-username/campus-event-manager-backend.git
   cd campus-event-manager-backend

2. **Create a virtual environment**
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3.**Install dependencies**
    pip install -r requirements.txt
    
4.**Run migrations**
    python manage.py migrate
    
5.**Create a superuser**
    python manage.py createsuperuser
    
6.**Start the server**
    python manage.py runserver
    
7.**Access Admin Panel**
    Open http://127.0.0.1:8000/admin/ and log in with your superuser credentials.
    
---

## 🖼️ Screenshots
📌 Admin Dashboard
![b1](https://github.com/user-attachments/assets/0cc1617f-66d7-4b52-8466-a2e280c4921e)
![bk1](https://github.com/user-attachments/assets/cc9a56fc-2d10-4e95-a99a-a7d9d03f5024)

📝 Event Management
![BK4](https://github.com/user-attachments/assets/19963e87-2836-44d0-b0d8-239b2fa561c1)

📜 Certificate Upload
![bk3](https://github.com/user-attachments/assets/c7469ebb-f977-4c48-a84c-df9e858d94e9)

📣 Notice Control   
![bk5](https://github.com/user-attachments/assets/2ae4755d-2c95-4322-8e7f-4543cb2ccace)

---
## 📌 License
This project is developed for educational purposes and may be reused with credit.
