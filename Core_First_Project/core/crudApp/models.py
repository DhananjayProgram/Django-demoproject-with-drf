from django.db import models

# Create your models here.


class userDetail(models.Model):
    name = models.CharField(max_length=10)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name
