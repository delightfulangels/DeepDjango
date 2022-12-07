# DeepDjango
![183299199-6d1dbb7f-0412-4e8c-adec-283d41936c8a](https://user-images.githubusercontent.com/99844369/183653915-2f1c5617-967e-46d9-b0bc-29d822fdf582.png)

### Description
**Deep Django - Website with articles about Python and Django**<br>
This is the source code of my Django website which was created as a learning project. Its main purpose is to contain tutorials, guides, articles, news about Django Framework, Django REST Framework, and Python programming language. :snake:
### Features
- Custom user model, authorization using [django-allauth](https://github.com/pennersr/django-allauth)
- CRUD
- User profiles
- Uploading pictures, user avatars
- Comments on articles
- Categories
- Text formatting using [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor)
- Simple API, using [django-rest-framework](https://github.com/encode/django-rest-framework)<br>

In work:

- Unit-Tests for each application

### Install
- Clone this repository:<br>
`$ git clone https://github.com/delightfulangels/DeepDjango.git`
- Create virtual environment:<br>
`$ python3 -m venv .venv`
- Activate environment:<br>
`$ source .venv/bin/activate`
- Install the dependencies:<br>
`$ pip install -r requirements.txt`
- Run:<br>
`$ python manage.py runserver`

### Tests
With this command you can run tests:<br>
`$ python manage.py test`
