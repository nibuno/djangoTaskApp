# Generated by Django 4.2.9 on 2024-02-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="title",
            field=models.CharField(
                default="タイトル", max_length=100, verbose_name="タイトル"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="task",
            name="content",
            field=models.TextField(blank=True, verbose_name="本文"),
        ),
    ]
