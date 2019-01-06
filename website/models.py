from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    bodypart = models.CharField(max_length=100)
    movement = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return str(self.bodypart) +' '+ str(self.movement)

class Workout(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    type = models.CharField(max_length=100)
    complete = models.BooleanField(default = False)
    exercise = models.ManyToManyField(Exercise,blank = True)

    def __str__(self):
        return str(self.type) +' '+ str(self.date)
