from django.core.management.base import BaseCommand
from tasks.models import Task


class Command(BaseCommand):
    help = "Aggregate the total time of all tasks"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("未完了のタスク一覧を表示します"))
        for task in Task.objects.filter(status=0):
            self.stdout.write(self.style.SUCCESS(f"{task.title}"))
