from django.db import models


class Tool(models.Model):

    identifier = models.CharField(max_length=50)
    name = models.CharField(max_length=100)


class Revision(models.Model):

    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    date = models.DateField()
    test_engineer = models.CharField(max_length=100)
    pending = models.BooleanField()
