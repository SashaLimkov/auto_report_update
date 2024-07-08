from django.core.management import BaseCommand
from redmine.rw_db import get_all_users
from employers.services import telegram_employer as ew

class Command(BaseCommand):
    help = "fill redmine employers"

    def handle(self, *args, **options):
        users = get_all_users()
        for user in users:
            ew.create_telegram_employer(**user)
        print("done")
