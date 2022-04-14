# Most basic Django API

Most basic Django backend (with a music theme) which just returns a simple JSON response.

The JSON response can be reached at <http://127.0.0.1:8000/api/albums/>

<img width="417" alt="image" src="https://user-images.githubusercontent.com/1945462/163543877-df4e9539-5742-4bc6-b291-e7f6b3083ca4.png">

## Run

1. Clone the repo.
2. Make sure you have [poetry](https://python-poetry.org/) (python environment and dependency manager) installed.
3. In the project folder run `poetry install` to install dependencies.
4. Run `poetry shell` to open a new shell with all dependencies available.
5. Run `python manage.py runserver`
6. Go to <http://127.0.0.1:8000/api/albums/> to view the JSON response

## Re-create this project

Check out [HOW_TO.md](./HOW_TO.md) to see how this project got created step-by-step