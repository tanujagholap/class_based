from django.db import models


class Create(models.Model):
    f_name = models.CharField(max_length=20)
    s_name = models.CharField(max_length=20)
    roll = models.IntegerField()
    subject = models.CharField(max_length=20)
