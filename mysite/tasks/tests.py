import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from .models import Task
from datetime import date


@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="12345")


@pytest.fixture
def client(user):
    client = Client()
    client.force_login(user)
    return client


@pytest.mark.django_db
def test_create_task(client):
    # arrange
    url = reverse("task_create")

    # act
    response = client.post(
        url,
        {
            "title": "テストタイトル",
            "content": "テストコンテンツ",
            "limit_date": "2024-04-23",
            "status": 0,
        },
    )

    # assert
    assert response.status_code == 302
    assert Task.objects.count() == 1
    task = Task.objects.first()
    assert task.title == "テストタイトル"
    assert task.content == "テストコンテンツ"
    assert task.limit_date == date(2024, 4, 23)
    assert task.status == 0
