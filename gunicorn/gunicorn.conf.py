# Config gunicorn

bind = "0.0.0.0:8888"

worker = 4

wsgi_app = "backend.wsgi:application"

# Config ssl cert
certfile = "ssl/cert.pem"
keyfile = "ssl/key.pem"
secure_scheme_headers = {"X-Forwarded-Proto": "https"}
