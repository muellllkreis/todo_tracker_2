from django.db import models

class Todo(models.Model):
    todo_text = models.CharField(max_length=160)
    todo_date = models.CharField(max_length=40)
    todo_progress = models.IntegerField(default=0)

    def __str__(self):
        return self.todo_text
