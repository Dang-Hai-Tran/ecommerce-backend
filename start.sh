#!/bin/bash

# Cheking if keys folder exists
if [ ! -d "keys" ]; then
    mkdir keys
fi

# Check if keys/private_key.pem exists
if [ ! -f "keys/private_key.pem" ]; then
    openssl genrsa -out keys/private_key.pem 2048
fi

# Check if keys/public_key.pem exists
if [ ! -f "keys/public_key.pem" ]; then
    openssl rsa -in keys/private_key.pem -pubout -out keys/public_key.pem
fi

# Check if ssl folder exists
if [ ! -d "ssl" ]; then
    mkdir ssl
fi

# Create ssl certificate
if [ ! -f "ssl/cert.pem" ] || [ ! -f "ssl/key.pem" ]; then
    openssl req -x509 -newkey rsa:4096 -keyout ssl/key.pem -out ssl/cert.pem -days 365 -nodes -subj "/C=FR/ST=Ile-de-France/L=Paris/O=42/CN=localhost"
fi

source /Users/datran/.local/share/virtualenvs/ecommerce-wOAtAchP/bin/activate

cd /Users/datran/learn_devs/fullstack/ecommerce

gunicorn -c gunicorn/gunicorn.conf.py
