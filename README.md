# Sohojogi Recommendation API

This Flask application provides endpoints to recommend user stories and expert talks based on user IDs. 

## Overview

The application has two main endpoints:

1. **Get User Stories** (`/get_user_stories`): 
   - Method: `POST`
   - Description: Recommends stories to a user based on their viewing history.
   - Request Body: JSON object containing the user ID.
   - Response: JSON array of recommended stories.

2. **Get User Talks** (`/get_user_talks`): 
   - Method: `POST`
   - Description: Recommends expert talks to a user based on their viewing history.
   - Request Body: JSON object containing the user ID.
   - Response: JSON array of recommended talks.

### Example Usage

**Get User Stories**

- **Request**:
  ```json
  {
    "userid": "123"
  }
  ```
- **Response**: JSON array of recommended stories.

**Get User Talks**

- **Request**:
  ```json
  {
    "userid": "123"
  }
  ```
- **Response**: JSON array of recommended talks.
