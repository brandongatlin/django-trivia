from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    category_name = models.CharField(default='Misc', max_length=50)
    def __str__(self):
        return self.category_name


class Question(models.Model):
    text = models.CharField(default='', max_length=50)
    answer = models.CharField(max_length=30, default=None)
    is_true_false = models.BooleanField(default=False)
    options = ArrayField(models.CharField(max_length=30))
    image = models.ImageField(upload_to='questionimages/', default='default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Score(models.Model):
    player_name = models.CharField(default='ANON', max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    feedback_text = models.CharField(default='', max_length=50)
    is_positive = models.BooleanField(default=True)


