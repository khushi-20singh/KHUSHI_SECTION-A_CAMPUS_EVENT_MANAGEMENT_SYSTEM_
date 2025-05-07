
# 🎓CAMPUS EVENT MANAGEMENT SYSTEM (Admin Backend)

A Django-powered backend platform that streamlines campus event coordination by enabling admins to manage users, events, certificates, and notices—all from a centralized dashboard. Designed for efficient campus operations and easy access to academic and extracurricular records.

---

## 📽️ Demo Video
[Watch Demo](https://your-demo-video-link.com)

## 📄 Project Report
[View Project Report (PDF)](https://your-project-report-link.com)

## 📊 Presentation Slides
[View Presentation (PDF)](https://your-presentation-link.com)

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
Project Structure
campus_event/
│
├── campus_event/ # Main project config (settings, urls)
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── event_management/ # Main app (models, views, admin)
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── migrations/
│
├── media/ # Uploaded certificates, notices
├── db.sqlite3 # SQLite database
└── manage.py # Runserver entry point
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
