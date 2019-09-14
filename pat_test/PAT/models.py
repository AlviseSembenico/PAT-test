from django.db import models


class Tool(models.Model):

    identifier = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    pending = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    classID = models.IntegerField('class')

    def __str__(self):
        return self.identifier


class Revision(models.Model):

    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    date = models.DateField()
    visual_check = models.IntegerField(choices=[
        (1, 'Pass'),
        (2, 'Fail')
    ])
    earth = models.CharField(max_length=100)
    leakage = models.CharField(max_length=100)
    insulation = models.CharField(max_length=100)
    function_check = models.IntegerField(choices=[
        (1, 'Pass'),
        (2, 'Fail')
    ])
    result = models.IntegerField(choices=[
        (1, 'Pass'),
        (2, 'Fail')
    ])
    test_engineer = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True, default=None)
