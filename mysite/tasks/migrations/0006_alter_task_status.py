# Generated by Django 4.2.9 on 2024-03-09 22:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0005_task_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.IntegerField(
                choices=[(0, "まだ"), (1, "ぼちぼち"), (2, "おわった")],
                default=0,
                verbose_name="ステータス",
            ),
        ),
    ]
