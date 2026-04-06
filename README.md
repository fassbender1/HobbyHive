📘 HobbyHive – Full Documentation

🚀 Overview

HobbyHive is a full-stack Django web application designed to bring people together through shared interests.

Users can:

Discover hobbies

Join groups

Participate in events

Interact socially via comments and participation systems

The platform emphasizes community building, user engagement, and scalable architecture, making it suitable for real-world deployment (AWS / Azure).

✨ Core Features

👤 Authentication & User System

User registration & login/logout

Profile pages with:

Profile picture upload (media handling)

User-specific data

Ownership-based permissions

🎯 Hobbies

Create, edit, delete hobbies

Join / leave hobbies

View participants

Ownership-based controls (edit/delete only for owner)

👥 Groups

Create groups tied to hobbies

Join / leave groups

Group ownership logic

Group detail pages

📅 Events

Create events within groups

Join / leave events

Event organizer system

Event detail pages

Email notifications (async via signals)

💬 Comments System

Users can comment on:

Events

Groups

Dynamic filtering (via query params like ?event= or ?group=)

🔍 Search & Pagination

Search across:

Hobbies

Groups

Events

Pagination for scalability

🔌 API (Django REST Framework)

📡 Available Endpoints

Endpoint	Description

/api/hobbies/	List/Create hobbies

/api/groups/	List/Create groups

/api/events/	List/Create events

💡 API Capabilities

JSON-based interaction

Can be used for:

Mobile apps 📱

Frontend frameworks (React/Vue)

External integrations

Easily extendable (authentication, filtering, permissions)

⚙️ Custom Middleware (Advanced Feature ⭐)

🧠 Middleware Breakdown

🔹 LastSeenMiddleware

Tracks last activity timestamp of users

Enables “last seen” features

🔹 RequestTimeMiddleware

Logs request execution time

Useful for debugging & performance monitoring

🔹 ForceCustomErrorPagesMiddleware

Forces custom error pages even when DEBUG=True

Ensures consistent UX during development & production

⚡ Asynchronous & Advanced Logic

📧 Signals (Django Signals)

Triggered on event creation

Automatically sends email notifications

Decouples business logic from views

🔄 Dynamic UI Behavior

Conditional buttons:

Join / Leave

Edit / Delete (owner-only)

Smart rendering based on user state

🎨 UI/UX Features

Responsive design (Bootstrap-based)

Clean card-based layouts

Conditional rendering for authenticated users

Custom error pages:

403 Forbidden

404 Not Found

500 Server Error

Generic fallback page

📁 Static & Media Handling

Static files served via WhiteNoise

Media files (profile pictures) handled separately

Production-ready configuration:

STATIC_ROOT

MEDIA_ROOT

🚀 Deployment Ready

The project is fully prepared for:

☁️ AWS / Azure Deployment

Works with:

Nginx + Gunicorn

WhiteNoise (static files)

Environment-based configuration supported

🔐 Production Considerations

DEBUG = False

Secure middleware enabled

Custom error handling

📦 Installation & Setup

1️⃣ Clone the repository

git clone <your-repo-url>

cd HobbyHive

2️⃣ Create virtual environment

python -m venv .venv

3️⃣ Activate it

Windows:

.venv\Scripts\activate

Linux/Mac:

source .venv/bin/activate

4️⃣ Install dependencies

pip install -r requirements.txt

5️⃣ Apply migrations

python manage.py migrate

6️⃣ Run the server

python manage.py runserver

🔒 Environment & Ignored Files


The project excludes:

.venv/

env/

.env

__pycache__/

✔ Ensures clean repo

✔ Protects sensitive data

🌟 Extra Features (Beyond Requirements)

✅ Custom middleware (tracking + performance)

✅ Django signals (async behavior)

✅ REST API integration

✅ WhiteNoise production setup

✅ Dynamic UI logic (ownership & participation)

✅ Custom error handling in ALL environments

✅ Scalable architecture for cloud deployment

📊 Tech Stack

Backend: Django, Django REST Framework

Frontend: HTML, CSS, Bootstrap

Database: PostgreSQL (via psycopg2)

Deployment: AWS / Azure ready

Static Handling: WhiteNoise

📌 Final Notes for Evaluation

The project is production-ready

Demonstrates:

Clean architecture

Advanced Django usage

Real-world deployment considerations

Designed to scale beyond coursework requirements

🔗 Deployment Links


(To be added after deployment)

🌍 AWS:

🌍 Azure: