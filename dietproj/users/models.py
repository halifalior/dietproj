from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    age=models.IntegerField(default=18)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES,default=GENDER_MALE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    hight=models.DecimalField(max_digits=3, decimal_places=2)
    isveg=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def bmi(self):
        return 100

    def maxcal(self):
        return 1500