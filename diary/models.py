from django.db import models
from datetime import date
from django.utils import timezone

class Diary(models.Model):
    title = models.CharField("タイトル",max_length=30)
    contents = models.TextField("内容",blank=True)
    day = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title