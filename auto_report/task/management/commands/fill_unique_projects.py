from django.core.management import BaseCommand
from redmine.rw_db import get_all_projcts
from task.services import telegram_project as tp

class Command(BaseCommand):
    help = "fill redmine projects"

    def handle(self, *args, **options):
        tp.create_unique_projects()

