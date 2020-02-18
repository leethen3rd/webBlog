# Django Blog Application

## Creating a virtual enviroment to work in

`virtualenv "project name"`

### Activating on a MAc

`source .django_env/bin/activate`

### Acitivating on Windows

`source .django_env/Scripts/activate`

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

This will create a directory call webBlog. Within this directory will be a filed called manage.py and another directory called webBlog (Django names it the same as your project). This is called the **Project** directory.

### The manage.py file

This file is used to run all the commands for the Django server. All the command line commands will be run by the manage.py file.

## Run the Server

To check if everything was installed properly run the server locally to see if Django gives the default web page. This can be done by `cd` into the webBlog directory that has the manage.py file and run the following command:

```python
python manage.py runserver
```

_output:_

```
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 17, 2020 - 17:18:09
Django version 3.0.3, using settings 'webBlog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


```

## Create The Application

`cd webBlog` into the directory and create the application. In this case, it is called 'blog'.

```python
python manage.py startapp blog
```

<br>

# Add the Application to the Project

In order for Django to pick up the newly created application, it will need to be added to the `INSTALLED_APPS` list inside the settings.py file located ine the projects directory.
<br>
Do his by adding the name of the name of the class for AppConfig in the application's app.py file. In this example its in BlogConfig.

```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
```

Next - Add this to the project's settings.py file:

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # New application
    'blog.apps.BlogConfig',
]
```

The string added shows one of the installed apps is located at `blog.apps.BlogConfig()` which also gives the name to the application "blog"

# Creating Views

Views will need to be created inside the application directory. When views are created, they will need to be mapped so Django knows how to get to them.

In the blog directory. Add the code below to the views.py file.
This is a very basic view. Use this to just get a feel for how views work. Eventually these type of views will be replaced by templates.

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Blog Home</h1>')
```

## URLs File within Blog Directory

The `home` function created in the views.py file will need to be mapped to a URL. To do that, create a urls.py file in the blog directory.<br><br>
_Note: There is already a urls.py file in the webBlog directory but there needs to be one created in the blog directory_

## Mapping The View

### Note: This site is created to have the blog as the home page so and empty string will be used in the mapping.

Inside the new urls.py file, the code should follow what is below.

There are 2 import statements needed for this file. The first one can be copied from the urls.py file in the project directory. The import statement should look like this:

```python
from django.urls import path
```

The second import statement needs to import the home function from the views.py file that was created above. Since that file is in the same directory as this urls.py file, it can be written like this:

```python
from . import views
```

Also from the urls.py file in the project directory is the Python list variable called `urlpatterns`. This variable can also be copied to the urls.py file created in the blog directory and the path added to reflect the home view. The urls.py file in the blog directory should look like this:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
]
```

## URLPATTERNS Explained

- The path is from the first import statement. The `path()` function is used to map what is inside the function as a path.
- The blank quotation marks represents an empty string. This will be routed from the urls.py file in the project directory
- The naming in `urlpatterns` is used in order to perform URL reversing. It is best practice to choose names that will not clash with other applications choice of names within the same project. Use the appname prefix to help reduce this and as a best practice.

# Map the Project to the Application

In this case, the project urls.py file only shows the path to the admin portion of the blog site. In order to have the project look for the application urls they will have to be mapped/included in the urls.py file in the project directory.
<br>
The project urls.py file currently looks like this:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

The `include()` function needs to be imported from `django.urls` in order to include the new route that will be added in the `urlpatterns`.<br>
Next add the new path to the `urlpatterns` to include the blog urls. The file should look like this:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

<br>

# URL Mapping Logic

Django looks for the URL entered into the web browser in the urls.py file. Since some of the URLs being used for this application are located in the application's urls.py file, the path in the projects directory will `include()` a rout to that file.
<br>
In the example above. The second path in the project urls.py file is mapped like this:

```python
path('', include('blog.urls')),
```

An example of this is if the url inputted was www.yoursite.com <br>

- With nothing after the URL, Django considers this an empty string.
- Django will search the urls.py file in the project directory first. A match is found for an empty string in that file that routes django to the application's urls.py file sing the `include()` function.
- Django moves to the urls.py file in the application's directory and finds an empty string path mapped to the home view in the views.py file.
- This results in **Blog Home** being rendered into the web browser. This is from the from the views.py file where the home function was created>

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Blog Home</h1>')
```

<br>

# Add More Views

Add an about me view to the application.

### Add to the views.py file

Create an `about()` function in the views.py file like this:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

# New view for about me
def about(request):
    return HttpResponse('<h1>About Me</h1>')
```

### Map the New View

With the new view 'about' created in the views.py file, it needs to be mapped in the application's urls.py file like this:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
```

Notice there is no empty string for this path. The string 'about' will need to be added at the end of the URL to render the view. The forward slash `/` at the end of `about/` is needed to show Django that it is mapped like www.yoursite.com/about

### Check Views

- Check the new view by running the server with `python manage.py runserver`
- Type in `/about` at the end of the URL. The `about()` function from the views.py file should render the HTTP within that function.
- _Notice:_ Adding this view to the projects urls.py file is not needed. In the project's urls.py file, Django has a path to blog.urls via an empty string. Django will use this to match other URLs in the applications urls.py file.
  <br>
  <br>

# Templates

By default, Django looks for a template sub-directory in each application. Also within that directory, another directory is needed with the name of the application. This is so Django knows which templates are with which application. For small single app projects, this is not a big deal but for multi app projects this will need to be followed.

- Start by creating a directory in the blog application called templates
- Next, create another directory inside the new templates directory called blog

- All the template.html files will be placed in this directory

## Create Template Files

Inside the newly created directories, create 2 files called home.html and about.html. File structure should look something like this:

```
-webBlog
|
 -webBlog
 |
  -blog
  |
   -templates
   |
    -blog
    |
     -about.html
     -home.html
```

## Add HTML to the .html files

Add the html from the view functions into these templates

_home.html_

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Blog Template</title>
  </head>
  <body>
    <h1>Blog Home</h1>
  </body>
</html>
```

## Render the Templates

Templates are rendered in the views.py file with the help of the import statement

```python
from django.shortcuts import render
```

To render a template in this view, the HttpResponse import is no longer called. Instead the `home()` function will need to be written out like this:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Old HttpResponse Return
# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')


# Return Render the Template

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return HttpResponse('<h1>About Me</h1>')
```

To verify this worked. Look at the home.html template and notice the title is 'Blog Template". This should display in the application if this template was rendered properly.

## `render()` Arguments

When writing out a `render()` function like above. At least 2 arguments must be passed inside the function.

1. The `request` object
2. The template name with templates path - String format

There is a 3rd option argument for context

## Finish Adding Templates

After changing the `about()` function, the HttpResponse import statement can be removed. The new views.py file should look like this:

```python
from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
```

<br>

# Blog Functionality

In order to get the functionality of a blog like looping through blog post a for loop can be used in the template.

First add some data to the views.py file. This is only temporary since this will eventually be pulled from a database. For naw, just create dummy data at the top of the views.py file in dictionary form like this:

```python
from django.shortcuts import render

posts = [
    {
        'author': 'Michael Scott',
        'title': 'Blog Post One',
        'content': 'Nice to meet me!',
        'date_posted': 'March 10, 1983',
    },
    {
        'author': 'Jim Halpert',
        'title': 'Blog Post Two',
        'content': 'Ding Dong!',
        'date_posted': 'March 11, 1983',
    },
]
```

### Now use the optional 3rd argument for the `render()` function for context.

- The context variable has the key name 'posts' that can now be passed in the template

```python
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
```

## Template For Loop

The Django templating engine allows code to be written inside the template using code blocks.

- A code block is created by code insterted between `{% 2 curly braces and percent signs %}`

- In the `<body>` html tags of the template, a for loop can be written to call the dummy data created for post like this:

```python
<body>
    {% for post in posts %}
    {% endfor %}
</body>
```

- The `{% endfor %}` code block is needed to close out the loop in templates.
- Access the variables of a loop with `{{ double curly braces }}`
- The template has access to all the variables associated with the context variable by using the key 'posts'
- The full loop through the dummy data will look like this:

```python
  <body>
    {% for post in posts %}
    <h1>{{ post.title }}</h1>
    <p>By: {{ post.author }} on {{ post.date_posted }}</p>
    <p>{{ post.content }}</p>
    {% endfor %}
  </body>
```

## If Else Statements

These work the same as loops. Code blocks will look like this:

```python
{% if statement %}

{% else %}

{% endif %}
```
# Template Inheritance
Template inheritance is used to reduce the same code being written for multiple templates. A good example of this is the header and nav bar sections of a website. <br>
A base.html file can be used to solve this problem. 
