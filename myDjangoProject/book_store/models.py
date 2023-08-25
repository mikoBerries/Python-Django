from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify
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
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        # making a short {% url "book-detail" book.id %}
        return reverse("book-detail", args={self.slug})

    def save(self, *args, **kwargs):
        "overriding save method to completing slug field"

        # updating slug in books molde using slugify
        # self.slug = slugify(self.title)  # self.slug = this-is-title
        self.slug = "-".join((slugify(self.title), slugify(self.rating)))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
