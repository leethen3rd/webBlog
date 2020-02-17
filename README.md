# Django Blog Application

## Creating a virtual enviroment to work in

`virtualenv "project name"`

### Activating on a MAc

`source .django_env/bin/activate`

### Install requirments is requirement file is available

`pip install -r requirements.txt`

### If you have no requirements.txt - Install django with pip

`pip install django`

# Create Your Project

### This is the project directory that is being created. Not the application.

**The word webBlog is the name of this project**

```python
django-admin startproject webBlog
```

## Create The Application

`cd webBlog` into the directory and create the application. In this case, it is called 'blog'.

```python
python manage.py startapp blog
```

## Create your first view for the blog

In the blog directory. Add the code below to the views.py file.

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Blog Home</h1>')
```

This 'home' function created in the views.py file will need to be mapped to a URL. To do that, create a `urls.py` file in the blog directory.
_Note: There is already a `urls.py` file in the webBlog directory_
