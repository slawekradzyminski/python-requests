import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_albums():
    # given
    # no setup needed

    # when
    response = requests.get(f"{BASE_URL}/albums")

    # then
    assert response.status_code == 200
    albums = response.json()
    assert len(albums) == 100  # JSONPlaceholder has 100 albums
    assert isinstance(albums, list)
    assert all(isinstance(album, dict) for album in albums)

def test_get_single_album():
    # given
    album_id = 1

    # when
    response = requests.get(f"{BASE_URL}/albums/{album_id}")

    # then
    assert response.status_code == 200
    album = response.json()
    assert album["id"] == album_id
    assert "userId" in album
    assert "title" in album

def test_get_user_albums():
    # given
    user_id = 1

    # when
    response = requests.get(f"{BASE_URL}/users/{user_id}/albums")

    # then
    assert response.status_code == 200
    albums = response.json()
    assert isinstance(albums, list)
    assert all(album["userId"] == user_id for album in albums)

def test_create_album():
    # given
    new_album = {
        "userId": 1,
        "title": "Test Album"
    }

    # when
    response = requests.post(f"{BASE_URL}/albums", json=new_album)

    # then
    assert response.status_code == 201
    created_album = response.json()
    assert created_album["title"] == new_album["title"]
    assert created_album["userId"] == new_album["userId"]
    assert "id" in created_album 