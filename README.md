# Store API

This store API provides the following functionality:
- Manage sales
- Manage products
- Manage users
- Make daily closings
- Make a monthly balance

# Inside API folder


  ## Create a virtual environment
```bash
  python -m venv env
```

```bash
  env\Scripts\activate
```

  ## Install the requierements
```bash
  pip install -r requirements.txt
```

  ## Create database migration
```bash
  python manage.py makemigrations
```

  ## Applying migrations
```bash
  python manage.py migrate
```

  ## Run the project
```bash
  python manage.py runserver
```

Go to http://localhost:8000/
