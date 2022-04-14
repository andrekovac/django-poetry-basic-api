# How to create this repository

## SET UP AND INSTALLATION

1. Make sure `poetry` is installed.

2. Choose one of the options `A` or `B` (don't do both) to set up a `poetry` project:

*Alternative* **A**: **Poetry setup**

3. Run `poetry new django-poetry-basic-app` in the command line where you replace `django-poetry-basic-app` with the name of your choice.
4. Enter the folder (via `cd django-poetry-basic-app`).

*Alternative* **B**: **Poetry setup**

3. Create new folder (pick the name of your project folder) and open it in VSCode
4. Open a terminal and type `poetry init` <-- Running the `init` command will take you into an interactive session to define the parameters of your new project. Just hit **enter** on each question - this will use the defaults (in the `[]`).

**Install dependencies**

5. Install `django`: Run `poetry add django` in the new folder (should be `django` version `4.0.4`)
6. Install linter and code formatter (as dev dependencies): `poetry add --dev mypy autopep8`

**VSCode Setup**

7. Open the project folder in VSCode.

8. Open command palette (shortcut: `Cmd` + `Shift` + `P`) and type "*Python: Select Linter*" (without quotes) -> Hit **enter** and choose the option where it says **Poetry**.
9. Open command palette (shortcut: `Cmd` + `Shift` + `P`) and type "*Python: Select Interpreter*" (without quotes) -> hit **enter** and choose **mypy**. 

10. Delete the two following two folders with all of its contents:
    - `django_poetry_basic_app/` in case your project name is `django-poetry-basic-app`) - it will be called differently in your case.
    - `tests`

    Also rename `README.rst` into `README.md` and write a nice title 🙃

**Peotry shell**

11.  Run `poetry shell`. This opens a new shell environment in which we have access to everything we installed via poetry. In particular we can run django related commands.
12.  If you see something like `(django-poetry-basic-app-kOyYctIB-py3.9)`

**Notes**: 

- You can leave the shell by just typing `exit` and hitting enter.
- When you open a shell in **VSCode** you might directly end up in a poetry shell!

**New Django Project**

1.   Start a new Django project: `django-admin startproject backend .` (don't miss the dot `.` at the end - I picked the name `backend` for the folder - please stick with it)

**Start the app**

1.  Run `python manage.py runserver` (you can ignore warnings about missing migrations)
2.  Navigate to [http://localhost:8000/](http://localhost:8000/) in your browser -> If you see a page you've been successful! 🎉

**Note**: With `ctrl + c` you can stop the server.

**Make it a git repository**

1.   Run `git init` in the main project folder
2.   Create a file `.gitignore` in the main project folder with the contents of [this file](https://github.com/github/gitignore/blob/main/Python.gitignore)
3.   Add all files (`git add -A`) and make your initial commit (via `git commit -m "initial Django project setup"` or a similar message)
4.   Connect your project with a remote repository in GitHub

## Create new Django App `albums`

Make sure you're in a [poetry shell](https://python-poetry.org/docs/cli/#shell) and in the main project folder (with the `manage.py` file)

```sh
django-admin startapp albums
```

This will start us up an _app_, a small self-contained unit of models and logic that work together.
A less confusing term would be a _module_.

They can be ported and reused in different projects.

## Using an "app"/module

In order to use the app in our project, we have to reference it.

For this, we make a change to `settings.py` so that `albums` is counted among its `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'albums' # <-- Add this!
]
```

## Define the JSON response of the endpoint

In `albums/views.py` I create a function to return an album. Change this to return whatever your app is about. The file should then look like this:

```python
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def get_album(request):
    return JsonResponse({"name": "Beat it!", "artist": "Michael Jackson"})
```

## Define the url pattern for albums

Create an `albums/urls.py` file with the following content:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_album)
]
```

See that we're using the `get_album` function we defined before!

## Connect the albums endpoint to the entire project

In `backend/urls.py` add `path('albums/', include('albums.urls'))` to the `urlpatterns` right below the `admin/` path. It should then look like this:

```python
from django.contrib import admin
from django.urls import path, include # <-- add an `include` here!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('albums/', include('albums.urls')) # <-- add this line
]
```

## Test the request

1. Run the server via `python manage.py runserver`.
2. In your browser go to [http://127.0.0.1:8000/albums/](http://127.0.0.1:8000/albums/). Do you see a JSON response?

#### Insomnia or Postman

3. Set up a request collection in **Insomnia** or **Postman** and test a `GET` request to `http://127.0.0.1:8000/albums/`

## Git

Add all changes and make a new commit for this milestone.

**Bonus**: Check out [https://gitmoji.dev/](https://gitmoji.dev/) and copy a nice emoji to create a beatiful git message