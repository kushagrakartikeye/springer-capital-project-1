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
- [Screenshots](#screenshots)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

The **Employee Management System** is a RESTful API backend built using Django and Django REST Framework, designed to manage employee information, attendance, departments, and performance data with secure authentication and beautiful visual analytics.

---

## Features

- Token-based authentication for secure access
- Employee and department management (CRUD)
- Attendance tracking and reporting
- Performance metrics visualized with charts
- Comprehensive API documentation via Swagger and Redoc
- Data seeding commands for easy test data generation
- Modular and scalable Django apps structure

---

## Tech Stack

- Python 3.13
- Django 5.2.5
- Django REST Framework
- PostgreSQL (production), SQLite (local)
- drf-yasg for OpenAPI Documentation (Swagger/Redoc)
- Gunicorn as WSGI server for production
- Whitenoise for static file serving

---

## Installation

### Prerequisites

- Python 3.13 or later
- Git
- PostgreSQL (optional, for production)
- Virtual environment tool (`venv`, `virtualenv`)

### Steps

1. Clone the repository:

git clone https://github.com/kushagrakartikeye/springer-capital-project-1.git
cd springer-capital-project-1

text

2. Create and activate a virtual environment:

On Windows
python -m venv venv
venv\Scripts\activate

On macOS/Linux
python3 -m venv venv
source venv/bin/activate

text

3. Install dependencies:

pip install -r requirements.txt

text

---

## Configuration

1. Create a `.env` file from the example:

cp .env.example .env

text

2. Update `.env` with your settings such as:

SECRET_KEY=your-secret-key
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3

text

3. For production, set:

DATABASE_URL=postgres://username:password@host:5432/dbname
DJANGO_ALLOWED_HOSTS=yourdomain.com
DEBUG=False

text

---

## Usage

1. Apply migrations:

python manage.py migrate

text

2. Create a superuser to access admin:

python manage.py createsuperuser

text

3. Optionally seed test data:

python manage.py seed_data

text

4. Run development server:

python manage.py runserver

text

---

## API Documentation

- Swagger UI: [`/swagger/`](http://localhost:8000/swagger/)
- Redoc UI: [`/redoc/`](http://localhost:8000/redoc/)
- Raw JSON/YAML API schema available at `/swagger.json` or `/swagger.yaml`

---

## Seed Data

Populate the database with realistic sample data for testing:

python manage.py seed_data

text

---

## Testing

Run automated tests with:

python manage.py test

text

---

## Deployment

### Recommendations

- Use PostgreSQL for production
- Disable debug with `DEBUG=False`
- Correctly set `ALLOWED_HOSTS`
- Use Gunicorn to serve the app
- Whitenoise middleware to serve static files
- Set environment variables securely

---

## Screenshots

*Add these screenshots here, ideally in a folder named `screenshots/` in your repo.*

1. **Project Home Directory Structure**  
   Screenshot of your project root folder showing the structure (apps, settings, manage.py, etc.)
<img width="844" height="226" alt="Screenshot 2025-08-23 032942" src="https://github.com/user-attachments/assets/87b5377b-c47e-4c87-946a-4402c9372e50" />

2. **Virtual Environment Setup**  
   Screenshot of terminal commands creating and activating the virtual environment.
<img width="1359" height="999" alt="Screenshot 2025-08-23 033120" src="https://github.com/user-attachments/assets/1bb8756d-ac8b-4140-8dd0-695eab7c697a" />

3. **Dependency Installation**  
   Screenshot of running `pip install -r requirements.txt`.
<img width="1900" height="621" alt="image" src="https://github.com/user-attachments/assets/4e313d90-b724-4b7e-8a72-3bf077af9f56" />

4. **Running Migrations**  
   Show successful `python manage.py migrate` output.
<img width="1187" height="131" alt="image" src="https://github.com/user-attachments/assets/09f18c42-ba48-4bae-abea-00ed23539b34" />

5. **Seed Data Running**  
   Screenshot showing `python manage.py seed_data` running and output.
<img width="958" height="63" alt="image" src="https://github.com/user-attachments/assets/73eb3cd6-6b39-40b9-add6-b3e56e78ffe2" />

6. **Running Server**  
   Screenshot of running the server and hitting API root with a sample API response.
<img width="1919" height="839" alt="Screenshot 2025-08-23 032958" src="https://github.com/user-attachments/assets/480eeb8e-2868-4d77-a383-3f504b24c4ae" />
<img width="1919" height="946" alt="Screenshot 2025-08-23 033017" src="https://github.com/user-attachments/assets/27ab8b63-a6da-4bfa-ae79-4abbb90ee808" />
<img width="1919" height="945" alt="Screenshot 2025-08-23 033035" src="https://github.com/user-attachments/assets/09c6139d-c4c6-4aba-8737-d155e95bc707" />

7. **Admin Login Page**  
   Screenshot of Django admin login page.
<img width="1919" height="951" alt="image" src="https://github.com/user-attachments/assets/747c4cdd-0a7b-4c24-a420-1ff3e2b5e7d3" />

8. **Swagger UI**  
   Screenshot showing API docs via Swagger.
<img width="1919" height="948" alt="Screenshot 2025-08-23 033059" src="https://github.com/user-attachments/assets/5384870b-bc02-4027-acb5-e3ca429b88bd" />

9. **Sample Employee API Response**  
   Screenshot of actual JSON response from employee list API endpoint.
<img width="610" height="604" alt="image" src="https://github.com/user-attachments/assets/1669c746-eaed-414b-b933-126070aae546" />

10. **Charts Page**  
    Screenshot of the rendered charts page visualizing employee statistics.
<img width="1919" height="942" alt="Screenshot 2025-08-23 033209" src="https://github.com/user-attachments/assets/7f8ccaa9-ac5a-4504-9e04-d328bd0ab40e" />
<img width="1919" height="948" alt="Screenshot 2025-08-23 033200" src="https://github.com/user-attachments/assets/ee0681a1-23dc-449b-bad2-51152eda23dc" />

---

## Contributing

Contributions welcome! Please fork the repo, create a feature branch, and submit a pull request explaining your changes.

---

## License

MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Author:** Kushagra Kartikeye  
- **GitHub:** [kushagrakartikeye](https://github.com/kushagrakartikeye)  
- **Email:** kushagra@example.com

---

Thank you for reviewing the Employee Management System project!

---

*Images*

Use markdown like this to embed screenshots inside README:

text

Ensure your screenshots folder is committed to the repo.

---

Let me know if you want me to help generate any of the screenshots or assist with writing deployment documentation next!
