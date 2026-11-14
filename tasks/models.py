from django.db import models


# Todo model: Django turns this class into the table "tasks_todo" in PostgreSQL.
# An auto-incrementing primary key called "id" is added automatically.
class Todo(models.Model):
    # Required title, stored as VARCHAR(150). Django enforces the 150 character limit.
    title = models.CharField(max_length=150)

    # Optional description. blank=True lets forms accept an empty value,
    # which is saved as an empty string ('') rather than NULL.
    description = models.TextField(blank=True)

    # Completion status. New tasks start as not completed.
    completed = models.BooleanField(default=False)

    # Set once, automatically, when the task is first saved.
    # auto_now_add also keeps this field out of forms, so users cannot edit it.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Default order for every query on this model:
        # unfinished tasks first (False sorts before True), then newest first ("-" = descending).
        ordering = ["completed", "-created_at"]

    def __str__(self):
        # Readable name for a task in the shell, admin and templates.
        return self.title
