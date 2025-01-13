import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_photos():
    # given
    # no setup needed

    # when
    response = requests.get(f"{BASE_URL}/photos")

    # then
    assert response.status_code == 200
    photos = response.json()
    assert len(photos) == 5000  # JSONPlaceholder has 5000 photos
    assert isinstance(photos, list)
    assert all(isinstance(photo, dict) for photo in photos)

def test_get_single_photo():
    # given
    photo_id = 1

    # when
    response = requests.get(f"{BASE_URL}/photos/{photo_id}")

    # then
    assert response.status_code == 200
    photo = response.json()
    assert photo["id"] == photo_id
    assert "albumId" in photo
    assert "title" in photo
    assert "url" in photo
    assert "thumbnailUrl" in photo

def test_get_album_photos():
    # given
    album_id = 1

    # when
    response = requests.get(f"{BASE_URL}/albums/{album_id}/photos")

    # then
    assert response.status_code == 200
    photos = response.json()
    assert isinstance(photos, list)
    assert all(photo["albumId"] == album_id for photo in photos)

def test_create_photo():
    # given
    new_photo = {
        "albumId": 1,
        "title": "Test Photo",
        "url": "https://via.placeholder.com/600/92c952",
        "thumbnailUrl": "https://via.placeholder.com/150/92c952"
    }

    # when
    response = requests.post(f"{BASE_URL}/photos", json=new_photo)

    # then
    assert response.status_code == 201
    created_photo = response.json()
    assert created_photo["title"] == new_photo["title"]
    assert created_photo["url"] == new_photo["url"]
    assert created_photo["thumbnailUrl"] == new_photo["thumbnailUrl"]
    assert "id" in created_photo 