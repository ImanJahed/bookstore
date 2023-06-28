# Pull base image
FROM python:3.10.4-slim-bullseye

# Set Environment Variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set Work Directory
WORKDIR /code

# Install Dependencies
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# Copy Project
COPY . .
