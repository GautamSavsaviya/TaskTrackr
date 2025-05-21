from django.db import models

# Create your models here.

STATUS = [
    ("TD", "todo"),
    ("IP", "in-progress"),
    ("DN", "done"),
]


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=2, choices=STATUS, default="TD")
    due_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
