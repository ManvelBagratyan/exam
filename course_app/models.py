from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    rate = models.FloatField(default = 0.0)
    count = models.IntegerField(default = 0)
    average_rate = models.FloatField(default = 0.0)

    def __str__(self):
        return self.title

    def add_rating(self, new_rating):
        self.rate += new_rating
        self.count += 1
        self.average_rate = self.rate / self.count
        self.save()

class Lecture(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    age = models.IntegerField()