# MART AFRICA
- **Overview**
This is my final project

- **Setup Django**
```bash
python -m venv venv  # create a virtuel environment
pip install -r requirements.txt  # install all requirements need for this project
# these are the commands i used to setup the project
django-admin startproject mart_africa
python manage.py startapp users  # for my user auth and management
python manage.py startapp products  # for products management
python manage.py startapp orders # for order management
python manage.py startapp categories
# Test Db connection
python manage.py dbshell
```
#### Project Structure 
- **mart_africa/**
- ├── requirements.txt
- ├── .env
- |-- README.md
- ├── mart_africa/
- │   ├── settings.py
- │   └── urls.py
- └── apps/
-    ├── accounts/     # User authentication
-   ├── products/     # Product management
-    ├── orders/       # Order processing
-   └── categories/     # Category handling

- Install drf-yasg for Swagger documentation.
Configure Swagger to automatically document all APIs. The documentation should be available at /swagger/.