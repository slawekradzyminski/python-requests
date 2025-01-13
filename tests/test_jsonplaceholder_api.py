import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    # given
    # no setup needed

    # when
    response = requests.get(f"{BASE_URL}/posts")

    # then
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 100  # JSONPlaceholder returns 100 posts
    assert isinstance(posts, list)
    assert all(isinstance(post, dict) for post in posts)

def test_get_single_post():
    # given
    post_id = 1

    # when
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    
    # then
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    assert "title" in post
    assert "body" in post
    assert "userId" in post

def test_create_post():
    # given
    new_post = {
        "title": "Test Post",
        "body": "This is a test post",
        "userId": 1
    }

    # when
    response = requests.post(f"{BASE_URL}/posts", json=new_post)

    # then
    assert response.status_code == 201
    created_post = response.json()
    assert created_post["title"] == new_post["title"]
    assert created_post["body"] == new_post["body"]
    assert created_post["userId"] == new_post["userId"]
    assert "id" in created_post

def test_update_post():
    # given
    post_id = 1
    updated_data = {
        "title": "Updated Title",
        "body": "Updated body",
        "userId": 1
    }

    # when
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_data)

    # then
    assert response.status_code == 200
    updated_post = response.json()
    assert updated_post["title"] == updated_data["title"]
    assert updated_post["body"] == updated_data["body"]
    assert updated_post["id"] == post_id

def test_delete_post():
    # given
    post_id = 1

    # when
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")

    # then
    assert response.status_code == 200
    assert response.text == "{}"  # JSONPlaceholder returns empty object for successful delete 