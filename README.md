# Indian-Bank-API

This project provides a **GraphQL API service** to query Indian bank branches data using Django and Graphene-Django.

It is built as part of a technical assignment for evaluation purposes.

---
# Project Structure

```plaintext
Indian-Bank-API/
├── .venv/                      # Virtual environment (can be ignored in version control)
├── bank_api/                   # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── schema.py               # GraphQL schema definitions using Graphene
│   ├── settings.py             # Project settings (uses SQLite by default)
│   ├── urls.py                 # URL routing (includes /gql endpoint)
│   └── wsgi.py
├── banks/                      # Django app for handling bank/branch models
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py               # Models for Bank and Branch
│   ├── tests.py
│   ├── views.py
│   ├── migrations/             # Auto-generated DB migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   └── management/             # Custom Django management commands
│       └── commands/
│           └── load_branches.py  # Script to load CSV data into DB
├── bank_branches.csv           # Dataset file used to populate the database
├── db.sqlite3                  # SQLite DB (auto-created after migrations)
├── manage.py                   # Django’s CLI utility
└── README.md                   # Project documentation
```




---
## 🚀 Features<br>
<br>
- GraphQL endpoint at `/gql`<br>
- Query bank branches, IFSC codes, and associated bank details<br>
- Backend built using Django and Graphene<br>
- Clean and scalable codebase<br>
- Database Used: SQLite (default Django DB)<br>
- Includes test cases for basic validations (`test.py`)<br>
<br>
---<br>
<br>
## 📂 Dataset Source<br>
<br>
Data used in this project comes from the open-source dataset provided at:<br>
[https://github.com/Amanskywalker/indian_banks](https://github.com/Amanskywalker/indian_banks)<br>
<br>
---<br>
🛠️ Tech Stack<br>
Language: Python 3.11<br>
Backend: Django<br>
GraphQL: Graphene-Django<br>
<br>
⚙️ Setup Instructions (Local)<br>
#1. Clone the repository<br>
git clone https://github.com/your-username/your-repo-name.git<br>
cd your-repo-name<br>
<br>
#2. Create virtual environment and install dependencies<br>
python -m venv venv<br>
source venv/bin/activate  # or venv\Scripts\activate on Windows<br>
<br>
#3. Database<br>
Database Used: SQLite (default Django DB)<br>
No manual setup required — SQLite runs out of the box and stores data in db.sqlite3.<br>
<br>
#4. Run migrations<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
<br>
#5. Run the server<br>
python manage.py runserver<br>
<br>
Access GraphQL interface at http://127.0.0.1:8000/gql.<br>
<br>
#6. Test the server<br>
python manage.py test





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
