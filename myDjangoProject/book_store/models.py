from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Adress(models.Model):
    " 1:1 adress information for author"
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def full_address(self):
        return f"{self.city} - {self.street} ({self.postal_code})"

    def __str__(self):
        return self.full_address()

    class Meta:
        " organize meta data of this class will show"
        verbose_name_plural = "adress entires"


class Author(models.Model):
    " Holding book author information"
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Adress, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    """book class extend models django"""
    title = models.CharField(max_length=50)
    # adding validator to rating using django validator
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")  # PROTECT / SET_NULL
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        # making a short {% url "book-detail" book.id %}
        return reverse("book-detail", args={self.slug})

    # auto fill saving a slug for new book save from code
    # def save(self, *args, **kwargs):
    #     "overriding save method to completing slug field"

    #     # creating slug routing with slugify module
    #     # self.slug = slugify(self.title)  # self.slug = this-is-title
    #     self.slug = "-".join((slugify(self.title), slugify(self.rating)))
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
