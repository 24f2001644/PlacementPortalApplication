<<<<<<< HEAD
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




Backend Setup
1. Navigate to Backend
cd backend
2. Create Virtual Environment
Windows
python -m venv venv

Activate:

venv\Scripts\activate
Linux/Mac
python3 -m venv venv

Activate:

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file inside the backend folder:

FLASK_APP=app:create_app

JWT_SECRET_KEY=your_secret_key

DATABASE_URL=sqlite:///placement.db

REDIS_URL=redis://localhost:6379/0
5. Initialize Database

Run:

flask db upgrade

The database will be created automatically.

6. Start Flask Backend

Run:

flask run

Backend will start at:

http://127.0.0.1:5000
Redis Setup

Start Redis server:

Windows
redis-server
Linux
sudo systemctl start redis

Check Redis:

redis-cli ping

Expected output:

PONG
Celery Setup

Celery requires a worker and beat scheduler.

Open two separate terminals.

Start Celery Worker

Inside backend folder:

celery -A celery_worker.celery worker --loglevel=info

For Windows:

celery -A celery_worker.celery worker --pool=solo --loglevel=info
Start Celery Beat

Open another terminal:

celery -A celery_worker.celery beat --loglevel=info
Frontend Setup

Open a new terminal.

Navigate to frontend:

cd frontend
Install Packages
npm install
Start Vue Development Server
npm run dev

Frontend will start at:

http://localhost:5173
Running Application

You need to run these services simultaneously:

Terminal 1

Redis

redis-server
Terminal 2

Flask Backend

cd backend
venv\Scripts\activate
flask run
Terminal 3

Celery Worker

cd backend
celery -A celery_worker.celery worker --pool=solo --loglevel=info
Terminal 4

Celery Beat

cd backend
celery -A celery_worker.celery beat --loglevel=info
Terminal 5

Vue Frontend

cd frontend
npm run dev
Access Application

Frontend:

http://localhost:5173

Backend API:

http://127.0.0.1:5000
Default Roles

The application supports:

Admin
Company
Student

Authentication is handled using JWT tokens.

Troubleshooting
Celery not connecting to Redis

Check Redis:

redis-cli ping

If output is not:

PONG

restart Redis.

Flask App Not Found

Set:

Windows:

set FLASK_APP=app:create_app

Linux/Mac:

export FLASK_APP=app:create_app
Port Already In Use

Backend:

flask run --port 5001

Frontend:

npm run dev -- --port 5174
Author

Talbiya Parveen
B.Tech Computer Science Engineering
PSIT Kanpur


You can directly save this as `README.md` in your repository root.
=======
# CommunityHelp
>>>>>>> e550c565266b78f388891f8faecd7a8e861c9ae0


Website:--
https://placement-portal-application-psi.vercel.app/