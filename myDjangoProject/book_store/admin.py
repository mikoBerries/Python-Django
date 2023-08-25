from django.contrib import admin
from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    "this is class to overring some rule to presenting in admin panel"
    # readonly_fields = ("slug",)
    # creating slug filds using title
    prepopulated_fields = {"slug": ("title",)}
    # creating filter able in django admin
    list_filter = ("author", "rating",)
    # things to display in django admin
    list_display = ("title", "author",)


admin.site.register(Book, BookAdmin)
