# Generated by Django 4.2.9 on 2024-03-07 22:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0004_task_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="order",
            field=models.IntegerField(default=0, verbose_name="並び順"),
        ),
    ]