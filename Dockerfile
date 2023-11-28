# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        nginx \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt to the working directory
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application code to the working directory
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

RUN python manage.py makemigrations \
&& python manage.py migrate 

# Create a user for running the application
RUN useradd -ms /bin/bash rencraft
USER rencraft

# Run Gunicorn
CMD gunicorn rencraft_backend.wsgi:application --bind 0.0.0.0:8000
