from django.db import models


class Tools(models.Model):

    identifier = models.CharField(max_length=50)
    name = models.CharField(max_length=100)


class Revision(models.Model):

    tool = models.ForeignKey(Tools, on_delete=models.CASCADE)
    date = models.DateField()
    test_engineer = models.CharField(max_length=100)
    pending = models.BooleanField()
