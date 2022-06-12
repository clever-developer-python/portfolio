from django.db import models

# Create your models here.


class mails(models.Model):
    email = models.CharField(max_length=1000000)