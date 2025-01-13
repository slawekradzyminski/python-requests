import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_users():
    # given
    # no setup needed

    # when
    response = requests.get(f"{BASE_URL}/users")

    # then
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 10  # JSONPlaceholder has 10 users
    assert isinstance(users, list)
    assert all(isinstance(user, dict) for user in users)

def test_get_single_user():
    # given
    user_id = 1

    # when
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    # then
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id
    assert "name" in user
    assert "username" in user
    assert "email" in user
    assert "address" in user
    assert "phone" in user
    assert "website" in user
    assert "company" in user

def test_create_user():
    # given
    new_user = {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com",
        "address": {
            "street": "Test Street",
            "suite": "Apt. 123",
            "city": "Test City",
            "zipcode": "12345-6789",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-234-567-8900",
        "website": "test.com",
        "company": {
            "name": "Test Company",
            "catchPhrase": "Test Catch Phrase",
            "bs": "test bs"
        }
    }

    # when
    response = requests.post(f"{BASE_URL}/users", json=new_user)

    # then
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["name"] == new_user["name"]
    assert created_user["email"] == new_user["email"]
    assert created_user["address"]["city"] == new_user["address"]["city"]
    assert "id" in created_user

def test_update_user():
    # given
    user_id = 1
    update_data = {
        "email": "newemail@example.com",
        "website": "newwebsite.com"
    }

    # when
    response = requests.patch(f"{BASE_URL}/users/{user_id}", json=update_data)

    # then
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["email"] == update_data["email"]
    assert updated_user["website"] == update_data["website"]
    assert updated_user["id"] == user_id 