from django.db import models

class Course(models.Model):
    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in hours")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="beginner")

    def __str__(self):
        return self.title
