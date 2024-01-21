import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-#s+woex0_%ba=6u05xp0bj@%bu^9ndt1ou&a5=02)*#pm)zf96"

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog.apps.BlogConfig",
    "user.apps.UserConfig",
    "general.apps.GeneralConfig",
    # 'django_ckeditor_5',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"

"""
customColorPalette = [
      {
          'color': 'hsl(4, 90%, 58%)',
          'label': 'Red'
      },
      {
          'color': 'hsl(340, 82%, 52%)',
          'label': 'Pink'
      },
      {
          'color': 'hsl(291, 64%, 42%)',
          'label': 'Purple'
      },
      {
          'color': 'hsl(262, 52%, 47%)',
          'label': 'Deep Purple'
      },
      {
          'color': 'hsl(231, 48%, 48%)',
          'label': 'Indigo'
      },
      {
          'color': 'hsl(207, 90%, 54%)',
          'label': 'Blue'
      },
  ]

CKEDITOR_5_FILE_STORAGE = BASE_DIR/'media/'

CKEDITOR_5_CONFIGS = {
  'default': {
      'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                  'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
  },
  'extends': {
      'blockToolbar': [
          'paragraph', 'heading1', 'heading2', 'heading3',
          '|',
          'bulletedList', 'numberedList',
          '|',
          'blockQuote',
      ],
      'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
      'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                  'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                  'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                  'insertTable',],
      'image': {
          'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                      'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
          'styles': [
              'full',
              'side',
              'alignLeft',
              'alignRight',
              'alignCenter',
          ]
      },
      'table': {
          'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
          'tableProperties', 'tableCellProperties' ],
          'tableProperties': {
              'borderColors': customColorPalette,
              'backgroundColors': customColorPalette
          },
          'tableCellProperties': {
              'borderColors': customColorPalette,
              'backgroundColors': customColorPalette
          }
      },
      'heading' : {
          'options': [
              { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
              { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
              { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
              { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
          ]
      }
  },
  'list': {
      'properties': {
          'styles': 'true',
          'startIndex': 'true',
          'reversed': 'true',
      }
  }
}
"""

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.User"
