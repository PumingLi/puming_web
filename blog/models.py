from django.db import models
from diet.models import NutritionDay
from datetime import date

class Review(models.Model):

    date = models.DateField(default=date.today)
    name = models.CharField(default="Unknown", max_length=100)
    resturant = models.CharField(default="Unknown", max_length=100)
    taste_rating = models.IntegerField(default=0)
    health_rating = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    review = models.TextField()
    images = models.FileField(null=True, default=None, upload_to='blog/')
    score = models.IntegerField(default=0)

    def __str__(self):

        return "%s %s" % (self.name, self.resturant)

class Comment(models.Model):

    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    name = models.CharField(default="Anonymous", max_length=100)
    comment = models.TextField()
    score = models.IntegerField(default=0)

    def __str__(self):

        return "%s" % (self.name)
