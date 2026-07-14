# Placement Portal Application

A web-based Placement Portal Application designed to simplify and automate campus placement activities. The system provides separate dashboards and functionalities for **Students, Companies, and Administrators** to manage placement drives, applications, approvals, and placement statistics.

---

## Features

### Authentication
- User registration and login
- JWT-based authentication
- Role-based access control
- Secure password hashing

### Student Module
- Student profile management
- View available placement drives
- Apply for placement opportunities
- Track application status
- Upload resume
- Export application records
- View notifications

### Company Module
- Company registration
- Company profile management
- Create and manage placement drives
- View student applications
- Update application status
- View selected students
- Close placement drives

### Admin Module
- Admin dashboard
- Approve/reject companies
- Manage students
- Manage placement drives
- Monitor applications
- View placement statistics
- Export placement records

---

## Technology Stack

### Backend
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-Bcrypt
- Flask-Migrate
- Redis
- Celery

### Frontend
- Vue.js
- Bootstrap 5
- Axios

### Database
- SQLite

---

## Project Structure


Placement-Portal-Application/

│
├── backend/
│
│ ├── app.py
│ ├── config.py
│ ├── extensions.py
│ │
│ ├── models/
│ │ ├── user.py
│ │ ├── student.py
│ │ ├── company.py
│ │ ├── placement_drive.py
│ │ ├── application.py
│ │ ├── notification.py
│ │ └── export_job.py
│ │
│ ├── routes/
│ │ ├── auth.py
│ │ ├── admin.py
│ │ ├── student.py
│ │ └── company.py
│ │
│ ├── services/
│ │ ├── auth_service.py
│ │ ├── admin_service.py
│ │ ├── student_service.py
│ │ └── company_service.py
│ │
│ └── api.yaml
│
└── frontend/
└── Vue.js Application


---

## Database Design

The application uses a relational database with the following main entities:

- User
- Student
- Company
- Admin
- Placement Drive
- Application
- Notification
- Export Job

### Relationships

- User has one Student/Company/Admin profile
- Company creates multiple Placement Drives
- Student applies to multiple Placement Drives
- Placement Drive receives multiple Applications
- User receives multiple Notifications

---

## Installation and Setup

### 1. Clone Repository

```bash
git clone <repository-url>

cd placement-portal-application
Backend Setup

Navigate to backend:

cd backend

Create virtual environment:

python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Configure Environment Variables

Create a .env file:

SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
DATABASE_URL=sqlite:///placement.db
Run Backend Server
python app.py

Backend will run at:

http://127.0.0.1:5000
Frontend Setup

Navigate to frontend:

cd frontend

Install dependencies:

npm install

Run development server:

npm run dev

Frontend will run at:

http://localhost:5173
API Documentation

The complete API documentation is available in:

api.yaml

The API includes endpoints for:

Authentication
Admin operations
Company management
Student operations
User Roles
Admin

Responsible for:

Approving companies
Managing placement activities
Monitoring applications
Viewing statistics
Company

Responsible for:

Creating placement drives
Managing applications
Selecting candidates
Student

Responsible for:

Maintaining profile
Applying for drives
Tracking applications
Future Enhancements
AI-based placement recommendations
Email notifications
Advanced analytics dashboard
Cloud deployment
Resume-based job matching
Author

Talbiya Parveen

B.Tech Computer Science Engineering

IIT Madras BS Degree (Data Science)
