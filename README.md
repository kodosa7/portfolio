# portfolio
Personal portfolio site made in Django, using jQuery elements.

## requirements
requirements.txt

## install
- extract the archive
- create venv in the project root dir
- run your database server
- create a database called 'portfolio'
- edit settings.py db login credentials
- do migrations ```python3 manage.py migrate```
- create your superuser ```python3 manage.py createsuperuser```
- additionally fill up your db with fixtures
```python3 manage.py loaddata db-fixture.json```

## run
- ```python3 manage.py runserver```
- go to http://127.0.0.1/8000 in your browser
- eventually edit your data in the admin section http://127.0.0.1:8000/admin

