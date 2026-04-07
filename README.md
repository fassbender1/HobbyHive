
📘 HobbyHive – Full Project Documentation

AWS deployed:

http://51.21.64.133/

---

🚀 Overview

HobbyHive is a full-stack Django web application designed to connect people through shared interests.

It allows users to discover hobbies, join groups, participate in events, and interact socially within a structured and scalable platform.

The project is built with real-world deployment in mind and is suitable for hosting on platforms like AWS or Azure.

---

✨ Core Functionalities

---

👤 Authentication & Accounts (/accounts/)

User registration (/accounts/register/)

Login / Logout (/accounts/login/)

Profile view (/accounts/profile/<id>/)

Profile picture upload (media handling)

Profile edit (/accounts/profile/<id>/edit/)

Ownership-based permissions

---

🎯 Hobbies (/hobbies/)

List all hobbies

Create hobby (/hobbies/create/)

Edit hobby (/hobbies/<id>/edit/)

Delete hobby (/hobbies/<id>/delete/)

Join / Leave hobby

View hobby details (/hobbies/<id>/)

View participants

---

👥 Groups (/groups/)

List all groups

Create group (/groups/create/)

Edit group (owner only)

Delete group (owner only)

Join / Leave group

Group detail view (/groups/<id>/)

Groups are linked to hobbies

---

📅 Events (/events/)

List all events

Create event (/events/create/)

Edit event (organizer only)

Delete event (organizer only)

Join / Leave event

Event detail view (/events/<id>/)

Events belong to groups

Organizer system

---

💬 Comments System (/comments/)

Users can comment on:

Events

Groups

Dynamic filtering via query params:

/comments/?event=<id>

/comments/?group=<id>

---

🔍 Search & Pagination

Search functionality on:

Hobbies

Groups

Events

Pagination implemented across list views

---

🔌 API (Django REST Framework)

📡 Endpoints

/api/hobbies/

/api/groups/

/api/events/

---

💡 API Capabilities

JSON-based responses

Supports CRUD operations

Can be used for:

Mobile applications

Frontend frameworks (React, Vue, etc.)

External integrations

---

⚙️ Custom Middleware (Advanced Feature)

---

🧠 Implemented Custom Middlewares

LastSeenMiddleware

Tracks the last activity timestamp of authenticated users

RequestTimeMiddleware

Measures and logs request processing time (useful for performance monitoring)

ForceCustomErrorPagesMiddleware

Forces custom error pages (403, 404, 500) to display even when DEBUG=True

⚡ Asynchronous & Advanced Features

---

📧 Django Signals

Automatically triggered on event creation

Sends email notifications

Decouples logic from views

---

🔄 Dynamic UI Logic

Conditional rendering based on:

Ownership (Edit/Delete buttons)

Participation (Join/Leave buttons)

---

💡 Additional Enhancements
Smart templates for authenticated vs anonymous users

Query-based filtering for comments

Clean separation of concerns across apps

---

🎨 UI & User Experience

Responsive design (Bootstrap)

Card-based layout for all entities

User-friendly navigation

Conditional buttons based on permissions

Clean and minimal interface

---

⚠️ Custom Error Pages

Custom error pages implemented for:

403 – Forbidden

404 – Not Found

500 – Server Error

Generic fallback error page

These work in both development and production via middleware.

---

📁 Static & Media Handling

Static files served via WhiteNoise

Media files (profile pictures) handled via MEDIA_ROOT

Production-ready setup

---

🚀 Deployment Ready

The project is prepared for deployment on AWS using:

- Gunicorn as the WSGI server

- Nginx as a reverse proxy for static/media files and security

---

🔧 Production Setup Includes

DEBUG = False support

WhiteNoise for static files

Media file handling

Custom error pages

Secure middleware configuration

---

📦 Installation & Setup

1️⃣ Clone repository

git clone <your-repo-url>

cd HobbyHive

2️⃣ Create virtual environment

python -m venv .venv

3️⃣ Activate environment

Windows

.venv\Scripts\activate

Linux / Mac

source .venv/bin/activate

4️⃣ Install dependencies

pip install -r requirements.txt

5️⃣ Apply migrations

python manage.py migrate

6️⃣ Run server

python manage.py runserver

---

🔒 Ignored Files

The project excludes:

.venv/

env/

.env

__pycache__/

media/

---

🌟 Features Beyond Requirements

Custom middleware (tracking + performance)

Django signals (async logic)

REST API integration

WhiteNoise production configuration

Dynamic UI rendering (ownership & participation)

Custom error handling in all environments

Scalable deployment-ready architecture

---

📊 Tech Stack

Backend: Django, Django REST Framework

Frontend: HTML, CSS, Bootstrap

Database: PostgreSQL (psycopg2)

Deployment: AWS ready

Static handling: WhiteNoise

---

🔗 Deployment Links


AWS: http://51.21.64.133/

---

📌 Final Notes

This project demonstrates:

Full-stack Django development

Clean architecture and separation of concerns

Real-world deployment readiness

Advanced Django features beyond the basic requirements
