# Creating a REST API using Django REST Framework ('DRF')

Setup Instructions:

1. Create and activate virtual environment

```
python -m venv <name of virtual env>
source <name of virtual env>/bin/activate
```

2. Install Django: https://docs.djangoproject.com/en/4.2/
```
pip install Django==<latest_version>
django-admin startproject <name of project>
```

3. Start Application
```
python manage.py startapp watchlist_app
```

4. Start Dev Server
```
python manage.py runserver
```

5. Migrations and Creating Super User
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
