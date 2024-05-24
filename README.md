# Shojogi App Recommendation System

This Flask application integrates with Supabase and OpenAI GPT-3.5 to provide personalized content recommendations based on the user's viewing history.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.7+
- pip (Python package installer)
- A Supabase account and project
- An OpenAI account with API access

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/flask-supabase-recommendation-system.git
cd flask-supabase-recommendation-system
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_supabase_url`, `your_supabase_key`, and `your_openai_api_key` with your actual Supabase and OpenAI credentials.

## Usage

1. Start the Flask application:

```bash
flask run
```

By default, the application will run on `http://127.0.0.1:5000/`.

## API Endpoints

### GET /get_user_stories

Retrieve user stories and get content recommendations.

**Request Parameters:**

- `userid` (required): The ID of the user.

**Sample Request:**

```http
GET http://127.0.0.1:5000/get_user_stories?userid=123
```

**Sample Response:**

```json
[
    {
        "id": "4",
        "type": "article",
        "title_eng": "The Journey of AI",
        ...
    },
    ...
]
```

**Error Responses:**

- `400 Bad Request`: User ID is required.
- `404 Not Found`: User not found.
- `500 Internal Server Error`: Database query failed.
