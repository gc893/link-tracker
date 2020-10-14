from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

TYPES = (
    ('t', 'Tutorial'),
    ('d', 'Documentation'),
    ('a', 'Support Article')
)

STATUS = (
    ('n', 'New'),
    ('f', 'Favorite'),
    ('v', 'Viewed')
)

NOTE_TYPE = (
    ('p', 'Possitive'),
    ('n', 'Negative'),
    ('q', 'Question')
)

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    avatar = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Link(models.Model):
    address = models.CharField(max_length=255)
    title = models.CharField(max_length=150)
    link_type = models.CharField(max_length=1, choices=TYPES, default=TYPES[0][0])
    tags = models.CharField(max_length=150, null=True)
    created_date = models.DateField('Created on', default=date.today)
    planned_date = models.DateField('Planned for', null=True)
    viewed_date = models.DateField('Viewed on', default=date.today)
    github_project = models.CharField(max_length=255, null=True)
    code_snippet = models.TextField(max_length=500, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default=STATUS[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_date']

class Note(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=500)
    note_type = models.CharField(max_length=1, choices=NOTE_TYPE, default=NOTE_TYPE[0][0])
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
