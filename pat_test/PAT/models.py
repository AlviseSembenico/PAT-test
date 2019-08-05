from django.db import models


class Tool(models.Model):

    identifier = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.identifier


class Revision(models.Model):

    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    date = models.DateField()
    result = models.IntegerField(choices=[
        (1, 'Pass'),
        (2, 'Fail')
    ])
    test_engineer = models.CharField(max_length=100)
    pending = models.BooleanField(default=False)
