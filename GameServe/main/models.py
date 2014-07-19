from django.db import models

# Create your models here.
class Main(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
