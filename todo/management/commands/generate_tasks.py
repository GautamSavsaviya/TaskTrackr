from django.core.management.base import BaseCommand, CommandError
from todo.models import Todo
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = "Generate fake tasks."

    def add_arguments(self, parser):
        parser.add_argument(
            "no-task", nargs="?", type=int, default=1, help="No of tasks generate."
        )

    def handle(self, *args, **options):
        try:
            no_tasks = options["no-task"]
            for _ in range(no_tasks):
                task = Todo.objects.create(
                    title=fake.sentence(nb_words=5),
                    description=fake.text(max_nb_chars=10),
                    status=random.choice(seq=["TD", "IP", "DN"]),
                    due_date=fake.date_between(start_date="today", end_date="+1M"),
                )

                self.stdout.write(self.style.SUCCESS(f"Task: {task.title[:-1]} generated."))
        except Exception as e:
            raise CommandError(e)
