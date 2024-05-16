# Config gunicorn

bind = "0.0.0.0:8888"

worker = 4

wsgi_app = "backend.wsgi:application"

from backend.settings import STATIC_ROOT

static_files = {
    "/static": STATIC_ROOT,
}
