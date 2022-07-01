from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

APPS = [
    "home",
    "about",
    "contact",
]

ROOT_URLCONF = "kelodraken.config.urls"

WSGI_APPLICATION = "kelodraken.config.wsgi.application"
