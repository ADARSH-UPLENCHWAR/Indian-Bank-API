# Indian-Bank-API

This project provides a **GraphQL API service** to query Indian bank branches data using Django and Graphene-Django.

It is built as part of a technical assignment for evaluation purposes.

---
# Project Structure

Indian-Bank-API/<br>
├── .venv/                      # Virtual environment (can be ignored in version control)<br>
├── bank_api/                   # Django project configuration<br>
│   ├── __init__.py<br>
│   ├── asgi.py<br>
│   ├── schema.py               # GraphQL schema definitions using Graphene<br>
│   ├── settings.py             # Project settings (uses SQLite by default)<br>
│   ├── urls.py                 # URL routing (includes /gql endpoint)<br>
│   └── wsgi.py<br>
├── banks/                      # Django app for handling bank/branch models<br>
│   ├── __init__.py<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py               # Models for Bank and Branch<br>
│   ├── tests.py<br>
│   ├── views.py<br>
│   ├── migrations/             # Auto-generated DB migrations<br>
│   │   ├── 0001_initial.py<br>
│   │   └── __init__.py<br>
│   └── management/             # Custom Django management commands<br>
│       └── commands/<br>
│           └── load_branches.py  # Script to load CSV data into DB<br>
├── bank_branches.csv           # Dataset file used to populate the database<br>
├── db.sqlite3                  # SQLite DB (auto-created after migrations)<br>
├── manage.py                   # Django’s CLI utility<br>
└── README.md                   # Project documentation<br>






---

## 🚀 Features

- GraphQL endpoint at `/gql`
- Query bank branches, IFSC codes, and associated bank details
- Backend built using Django and Graphene
- Clean and scalable codebase
- Database Used: SQLite (default Django DB)
- Includes test cases for basic validations(test.py)

---

## 📂 Dataset Source

Data used in this project comes from the open-source dataset provided at:
[https://github.com/Amanskywalker/indian_banks](https://github.com/Amanskywalker/indian_banks)

---
🛠️ Tech Stack
Language: Python 3.11
Backend: Django
GraphQL: Graphene-Django

⚙️ Setup Instructions (Local)
#1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

#2. Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

#3.Database
Database Used: SQLite (default Django DB)
No manual setup required — SQLite runs out of the box and stores data in db.sqlite3.

#4. Run migrations
python manage.py makemigrations
python manage.py migrate

#5. Run the server
python manage.py runserver

Access GraphQL interface at http://127.0.0.1:8000/gql.




## 🔗 GraphQL Sample Query

To get all branches with their IFSC codes and bank names:

```graphql
query {
  branches {
    edges {
      node {
        branch
        ifsc
        bank {
          name
        }
      }
    }
  }
}
