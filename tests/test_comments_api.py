import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_comments():
    # given
    # no setup needed

    # when
    response = requests.get(f"{BASE_URL}/comments")

    # then
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) == 500  # JSONPlaceholder has 500 comments
    assert isinstance(comments, list)
    assert all(isinstance(comment, dict) for comment in comments)

def test_get_single_comment():
    # given
    comment_id = 1

    # when
    response = requests.get(f"{BASE_URL}/comments/{comment_id}")

    # then
    assert response.status_code == 200
    comment = response.json()
    assert comment["id"] == comment_id
    assert "postId" in comment
    assert "name" in comment
    assert "email" in comment
    assert "body" in comment

def test_get_comments_by_post():
    # given
    post_id = 1

    # when
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")

    # then
    assert response.status_code == 200
    comments = response.json()
    assert isinstance(comments, list)
    assert all(comment["postId"] == post_id for comment in comments)

def test_create_comment():
    # given
    new_comment = {
        "postId": 1,
        "name": "Test Comment",
        "email": "test@example.com",
        "body": "This is a test comment"
    }

    # when
    response = requests.post(f"{BASE_URL}/comments", json=new_comment)

    # then
    assert response.status_code == 201
    created_comment = response.json()
    assert created_comment["name"] == new_comment["name"]
    assert created_comment["email"] == new_comment["email"]
    assert created_comment["body"] == new_comment["body"]
    assert "id" in created_comment 