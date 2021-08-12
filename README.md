
## Setup

The first thing to do is to clone the repository:

```
$ git clone https://github.com/AbolfazlAbdi48/email-sender.git
cd email-sender

```

Create a virtual environment to install dependencies in and activate it:

```
$ python -m venv venv
$ venv\scripts\activate

```

Then install the dependencies:

```
$ pip install django

```

Note the  `(venv)`  in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by  `virtualenv`.

Once  `pip`  has finished downloading the dependencies:

```
$ python manage.py runserver

```
setting.py:

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'    
    EMAIL_HOST = 'smtp.gmail.com'    
    EMAIL_HOST_USER = 'your email'    
    EMAIL_HOST_PASSWORD = 'your password'    
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

And navigate to  `http://127.0.0.1:8000`.
