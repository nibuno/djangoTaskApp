import factory
from tasks.models import Task
from django.contrib.auth.models import User
import datetime


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("テストユーザー")


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Faker("テストタイトル")
    content = factory.Faker("テストコンテンツ")
    status = 0
    order = factory.Sequence(lambda n: n)
    created_user = factory.SubFactory(UserFactory)
    limit_date = factory.LazyFunction(datetime.date.today)
    updated_user = factory.SubFactory(UserFactory)
    created_at = factory.LazyFunction(datetime.datetime.now)
    updated_at = factory.LazyFunction(datetime.datetime.now)
