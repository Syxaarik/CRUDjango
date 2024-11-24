from django.db import models


class Person(models.Model):
    objects = None
    DoesNotExist = None
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=35)

    def __str__(self):
        return self.second_name
