# Python API Testing Example

This repository contains example API tests for JSONPlaceholder using Python's requests library.

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

To run all tests:
```bash
pytest
```

To run tests with coverage report:
```bash
pytest --cov=tests
```

To run tests for a specific endpoint:
```bash
pytest tests/test_posts_api.py
pytest tests/test_comments_api.py
pytest tests/test_albums_api.py
pytest tests/test_photos_api.py
pytest tests/test_todos_api.py
pytest tests/test_users_api.py
```

## Test Cases

The test suite covers all JSONPlaceholder endpoints:

### Posts (/posts)
- Get all posts
- Get single post
- Create post
- Update post
- Delete post

### Comments (/comments)
- Get all comments
- Get single comment
- Get comments by post
- Create comment

### Albums (/albums)
- Get all albums
- Get single album
- Get user albums
- Create album

### Photos (/photos)
- Get all photos
- Get single photo
- Get album photos
- Create photo

### Todos (/todos)
- Get all todos
- Get single todo
- Get user todos
- Create todo
- Update todo completion status

### Users (/users)
- Get all users
- Get single user
- Create user
- Update user

All tests are performed against the JSONPlaceholder API (https://jsonplaceholder.typicode.com/) 