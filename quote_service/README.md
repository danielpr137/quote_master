# Quote Service

## Introduction

Quote Service is a FastAPI-based web application that provides a RESTful API for retrieving and managing quotes and author information. It allows users to fetch quotes from external sources, store them in a MongoDB database, and retrieve information about authors and their works from external APIs.

## Features

- Fetch quotes from external sources and store them in a MongoDB database.
- Retrieve stored quotes and display them through API endpoints.
- Fetch author information and book titles from external APIs and present them in a user-friendly format.
- Background task to fetch and store quotes periodically.
- Comprehensive test suite to ensure API functionality and behavior.

## Getting Started

### Installation

1. Clone the repository:
    git clone https://github.com/danielpr137/quote-service.git
    cd quote-service

2. Create a virtual environment and activate it:
    python3 -m venv venv
    source venv/bin/activate

3. Install the required dependencies:
    pip install -r requirements.txt


### Configuration

1. Create `.env` file:
    touch app/server/.env

2. Configure the MongoDB connection details in the `.env` file:
    MONGO_DETAILS = mongodb+srv://quotes_master:1vICqw9f8uJKUZpz@cluster0.uqdsnfv.mongodb.net/?retryWrites=true&w=majority

## Usage

1. Start the FastAPI application:
    uvicorn app.server:app --host 0.0.0.0 --port 8000

2. Access the API documentation at `http://localhost:8000/docs` or `http://localhost:8000/redoc`.

## API Endpoints

- `GET /api/v1/get-quotes`: Retrieve stored quotes.
- `GET /api/v1/fetch-quotes`: Fetch and store quotes in the background.
- `GET /api/v1/get-author-info`: Retrieve author information and book titles from open library API.

