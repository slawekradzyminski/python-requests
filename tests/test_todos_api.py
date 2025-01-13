import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_todos():
    # given
    # no setup needed

    # when
    response = requests.get(f"{BASE_URL}/todos")

    # then
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) == 200  # JSONPlaceholder has 200 todos
    assert isinstance(todos, list)
    assert all(isinstance(todo, dict) for todo in todos)

def test_get_single_todo():
    # given
    todo_id = 1

    # when
    response = requests.get(f"{BASE_URL}/todos/{todo_id}")

    # then
    assert response.status_code == 200
    todo = response.json()
    assert todo["id"] == todo_id
    assert "userId" in todo
    assert "title" in todo
    assert "completed" in todo
    assert isinstance(todo["completed"], bool)

def test_get_user_todos():
    # given
    user_id = 1

    # when
    response = requests.get(f"{BASE_URL}/users/{user_id}/todos")

    # then
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)
    assert all(todo["userId"] == user_id for todo in todos)

def test_create_todo():
    # given
    new_todo = {
        "userId": 1,
        "title": "Test Todo",
        "completed": False
    }

    # when
    response = requests.post(f"{BASE_URL}/todos", json=new_todo)

    # then
    assert response.status_code == 201
    created_todo = response.json()
    assert created_todo["title"] == new_todo["title"]
    assert created_todo["completed"] == new_todo["completed"]
    assert created_todo["userId"] == new_todo["userId"]
    assert "id" in created_todo

def test_update_todo_completion():
    # given
    todo_id = 1
    update_data = {
        "completed": True
    }

    # when
    response = requests.patch(f"{BASE_URL}/todos/{todo_id}", json=update_data)

    # then
    assert response.status_code == 200
    updated_todo = response.json()
    assert updated_todo["completed"] == update_data["completed"]
    assert updated_todo["id"] == todo_id 