from tasks.models import Task
import logging


def run():
    """commandsのnot_finished_task_listをrunscriptで試しに書き換えてみた
    docker compose run web python mysite/manage.py runscript not_finished_task_list
    """
    logging.basicConfig(level=logging.INFO)
    logging.info("未完了のタスク一覧を表示します")
    for task in Task.objects.filter(status=0):
        logging.info(task.title)
