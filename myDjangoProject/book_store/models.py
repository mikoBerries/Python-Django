from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
# Create your models here.


class Book(models.Model):
    """book class extend models django"""
    title = models.CharField(max_length=50)
    # adding validator to rating using django validator
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxLengthValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)


def __str__(self):
    return f"{self.title} ({self.rating})"
