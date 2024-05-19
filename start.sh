#!/bin/bash

# Cheking if keys folder exists
if [ ! -d "keys" ]; then
    echo "Creating keys folder"
    mkdir keys
fi

# Check if keys/private_key.pem exists
if [ ! -f "keys/private_key.pem" ]; then
    echo "Creating private key"
    openssl genrsa -out keys/private_key.pem 2048
fi

# Check if keys/public_key.pem exists
if [ ! -f "keys/public_key.pem" ]; then
    echo "Creating public key"
    openssl rsa -in keys/private_key.pem -pubout -out keys/public_key.pem
fi

# Check if ssl folder exists
if [ ! -d "ssl" ]; then
    echo "Creating ssl folder"
    mkdir ssl
fi

# Create ssl certificate
if [ ! -f "ssl/cert.pem" ] || [ ! -f "ssl/key.pem" ]; then
    echo "Creating ssl certificate"
    openssl req -x509 -newkey rsa:4096 -keyout ssl/key.pem -out ssl/cert.pem -days 365 -nodes -subj "/C=FR/ST=Ile-de-France/L=Paris/O=42/CN=localhost"
fi

# Check if not CIPHER_KEY in .env file then add CIPHER_KEY = $(openssl rand -base64 32) in .env file
if [ -f ".env" ]; then
    if ! grep -q "CIPHER_KEY" .env; then
        CIPHER_KEY=$(openssl rand -base64 64 | tr -d '\n' | cut -c1-32)
        echo "CIPHER_KEY=\"$CIPHER_KEY\"" >> .env
        echo "CIPHER_KEY added to .env file"
    else
        echo "CIPHER_KEY already exists in .env file"
    fi
else
    echo ".env file not found"
fi

source /Users/datran/.local/share/virtualenvs/ecommerce-wOAtAchP/bin/activate

cd /Users/datran/learn_devs/fullstack/ecommerce

gunicorn --reload -c gunicorn/gunicorn.conf.py
