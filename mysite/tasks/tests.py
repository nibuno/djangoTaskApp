import json
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task
from datetime import date


@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="12345")


@pytest.fixture
def client(user, client):
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
    task = Task.objects.first()

    # assert
    assert response.status_code == 302
    assert Task.objects.count() == 1
    assert task.title == "テストタイトル"
    assert task.content == "テストコンテンツ"
    assert task.limit_date == date(2024, 4, 23)
    assert task.status == 0


@pytest.mark.django_db
def test_edit_task(client):
    # arrange
    from .factories import TaskFactory

    task = TaskFactory(
        title="編集前タイトル",
        content="編集前コンテンツ",
        limit_date=date(2024, 4, 23),
        status=0,
    )

    # act
    url = reverse("task_edit", kwargs={"pk": task.pk})

    response = client.post(
        url,
        {
            "title": "編集後タイトル",
            "content": "編集後コンテンツ",
            "limit_date": "2024-04-24",
            "status": 1,
        },
    )
    actual = Task.objects.get(pk=task.pk)

    # assert
    assert response.status_code == 302
    assert actual.title == "編集後タイトル"
    assert actual.content == "編集後コンテンツ"
    assert actual.limit_date == date(2024, 4, 24)
    assert actual.status == 1


@pytest.mark.django_db
def test_delete_task(client):
    # arrange
    from .factories import TaskFactory

    task = TaskFactory()

    # act
    url = reverse("task_delete", kwargs={"pk": task.pk})

    response = client.post(url)

    # assert
    assert response.status_code == 302
    assert Task.objects.count() == 0
    assert not Task.objects.filter(pk=task.pk).exists()


@pytest.mark.django_db
def test_first_list_view(client):
    # arrange
    from .factories import TaskFactory

    task1 = TaskFactory(
        status=0,
    )
    task2 = TaskFactory(
        status=1,
    )
    TaskFactory(
        status=2,
    )

    # act
    url = reverse("task_list")
    response = client.get(url)

    # assert
    assert response.status_code == 200
    assert len(response.context["tasks"]) == 2
    assert response.context["tasks"][0] == task1
    assert response.context["tasks"][1] == task2


@pytest.mark.django_db
def test_save_order(client):
    """並び順が適切に保存されることを確認する

    FIXME: parametrizeでtest_save_order_not_changeと一緒に書き直す
    """
    # arrange
    from .factories import TaskFactory

    task1 = TaskFactory()
    task2 = TaskFactory()

    # act
    url = reverse("save_order")
    response = client.post(
        url, json.dumps([task2.pk, task1.pk]), content_type="application/json"
    )

    # assert
    assert response.status_code == 200
    task1.refresh_from_db()
    task2.refresh_from_db()

    assert task2.order == 0
    assert task1.order == 1


@pytest.mark.django_db
def test_save_order_not_change(client):
    """並び順が変更されないことを確認する

    FIXME: parametrizeでtest_save_orderと一緒に書き直す
    """
    # arrange
    from .factories import TaskFactory

    task1 = TaskFactory(order=0)
    task2 = TaskFactory(order=1)

    # act
    url = reverse("save_order")
    response = client.post(
        url, json.dumps([task2.pk, task1.pk]), content_type="application/json"
    )

    # assert
    assert response.status_code == 200
    task1.refresh_from_db()
    task2.refresh_from_db()

    assert task2.order == 0
    assert task1.order == 1


@pytest.mark.django_db
def test_save_order_http_method_get(client):
    # arrange
    url = reverse("save_order")

    # act
    response = client.get(url)

    # assert
    assert response.status_code == 405
