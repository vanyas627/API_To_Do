# ToDo API Portfolio

A simple RESTful API service for a To-Do application built with Django REST Framework.  
Created as a portfolio project by **Ivan Sotsenko**.

---

##  Features

- JWT authentication (`/api/token/`)
- User registration
- CRUD operations for Tasks
- Filtering and ordering
- Pagination
- Validation in serializers
- Swagger documentation (`/swagger/`)
- Unit tests with `pytest`

---

##  Stack

- Python 3.12
- Django 5.x
- Django REST Framework
- SimpleJWT
- drf-yasg (Swagger)
- Pytest

---

##  Local Setup

```bash
# clone the repository
git clone https://github.com/vanyas627/api_to_do.git
cd API_PORTFOLIO

# create and activate virtual environment
python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows

# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# create superuser (optional)
python manage.py createsuperuser

# run server
python manage.py runserver
```

---

## Authentication (JWT)

- **Get access & refresh tokens**

POST /api/token/

{
  "username": "your_username",
  "password": "your_password"
}


- **Refresh access token** 

POST /api/token/refresh/

{
  "refresh": "refresh_token"
}


- **Use the access token with:**

Authorization: Bearer <access_token>

## Main Endpoints
| Method      | Endpoint       | Description                          |
|------------|----------------|--------------------------------------|
| POST       | /api/register/ | Register new user                     |
| POST       | /api/login/    | Login user (session)                  |
| GET        | /api/tasks/    | List tasks (with filters + pagination) |
| POST       | /api/tasks/    | Create task                           |
| GET        | /api/tasks/id/ | Retrieve task                         |
| PUT/PATCH  | /api/tasks/id/ | Update task                           |
| DELETE     | /api/tasks/id/ | Delete task                           |



## Filtering / Ordering / Pagination

Examples:

/api/tasks/?completed=true  
/api/tasks/?ordering=-created_at  
/api/tasks/?page=1


## API documentation

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/
