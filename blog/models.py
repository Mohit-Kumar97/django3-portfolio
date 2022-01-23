from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    date=models.DateField()