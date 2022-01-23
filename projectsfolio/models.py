from django.db import models
from django.db.models.fields import URLField

class Portfoliomodel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='projectsfolio/images/')
    url=URLField(blank=True)