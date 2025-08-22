# Employee Management System

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![Django Version](https://img.shields.io/badge/django-5.2.5-green.svg)](https://www.djangoproject.com/weblog/2024/jun/01/django-52-released/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Seed Data](#seed-data)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

The **Employee Management System** is a backend RESTful API built using Django and Django REST Framework to manage employee details, departments, attendance, and performance data. It includes authentication, authorization, detailed API endpoints, and beautifully rendered charts for visual analytics.

---

## Features

- User registration and token-based authentication
- Employee CRUD operations
- Department and Attendance management
- Performance tracking and statistics
- API documentation with Swagger UI and Redoc
- Auto data seeding commands for test data
- Responsive chart visualization of employee metrics
- Modular Django apps for scalability

---

## Tech Stack

- Python 3.13
- Django 5.2.5
- Django REST Framework (DRF)
- PostgreSQL (for production)
- SQLite (default for local development)
- drf-yasg for Swagger documentation
- Gunicorn for WSGI HTTP server (production)
- Whitenoise for serving static files

---

## Installation

### Prerequisites

- Python 3.13+
- Git
- PostgreSQL (optional, for production)
- Virtualenv or venv

### Steps

1. Clone the repo

git clone https://github.com/kushagrakartikeye/springer-capital-project-1.git
cd springer-capital-project-1

text

2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

text

3. Install dependencies

pip install -r requirements.txt

text

---

## Configuration

1. Create a `.env` file in the project root by copying `.env.example`

cp .env.example .env

text

2. Fill `.env` with your environment-specific settings such as:

SECRET_KEY=your-secret-key
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3

text

3. For production, configure `DATABASE_URL` with your PostgreSQL connection string, for example:

DATABASE_URL=postgres://username:password@host:5432/dbname
DJANGO_ALLOWED_HOSTS=yourdomain.com
DEBUG=False

text

---

## Usage

### Run migrations

python manage.py migrate

text

### Create a superuser (admin)

python manage.py createsuperuser

text

### Seed test data (optional)

python manage.py seed_data

text

### Run the development server

python manage.py runserver

text

### Access points

- API Root: `http://127.0.0.1:8000/api/`
- Admin panel: `http://127.0.0.1:8000/admin/`
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- Redoc Documentation: `http://127.0.0.1:8000/redoc/`
- Charts view (example): `http://127.0.0.1:8000/api/charts/`

---

## API Documentation

This project implements comprehensive API documentation using Swagger and Redoc through drf-yasg.

You can access:

- Swagger UI: `/swagger/`
- Redoc UI: `/redoc/`
- Raw schema (JSON/YAML): `/swagger.json` or `/swagger.yaml`

---

## Seed Data

We include a Django management command to populate the database with fake employees, departments, and attendance records for testing:

python manage.py seed_data

text

---

## Testing

- Run tests via Django test framework:

python manage.py test

text

---

## Deployment

### Production setup recommendations:

- Use PostgreSQL as the database.
- Set `DEBUG=False` in your production environment.
- Configure allowed hosts correctly in `.env`.
- Use Gunicorn as WSGI server.
- Use Whitenoise middleware for static files.
- Run migrations on your production server before starting app.

Refer to **deployment notes** in the repo or consult your cloud hosting provider for specific configurations.

---

## Contributing

Contributions, issues, and feature requests are welcome!

Please fork the repo, create a feature branch, and submit a pull request with descriptive information.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Author:** Kushagra Kartikeye
- **GitHub:** [kushagrakartikeye](https://github.com/kushagrakartikeye)
- **Email:** kushagrakartikeye@gmail.com

---

**Thank you for checking out the Employee Management System!**
