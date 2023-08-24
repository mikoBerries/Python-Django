from django.shortcuts import render

from .models import Book
# Create your views here.


def index(request):
    # Creating dumb book to DB
    # newbook = Book()
    # newbook.title = "the wizard"
    # newbook.rating = 1
    # newbook.author = "somebody"
    # newbook.is_bestselling = True
    # newbook.save()
    # all_book = Book.objects.all()
    return render(request, "book_store/index.html", {
        "books": all_book
    })
