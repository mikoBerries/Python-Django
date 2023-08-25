from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg, Max, Min
from .models import Book
# Create your views here.


def index(request):
    " Displaying all books with rating and min max avg rating"
    # Creating dumb book to DB
    # newbook = Book()
    # newbook.title = "book number2"
    # newbook.rating = 2
    # newbook.author = "author"
    # newbook.is_bestselling = False
    # newbook.save()

    # Book.objects.all().delete()

    # get all book withou filter
    all_book = Book.objects.all().order_by("-rating")
    total_book = all_book.count()

    # aggregate returning dictioranry
    avg_rating = all_book.aggregate(
        Avg("rating"),
        Min("rating"),
        Max("rating")
    )  # rating__avg, rating__min

    return render(request, "book_store/index.html", {
        "books": all_book,
        "total_books": total_book,
        "average_rating": avg_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    # simplify code in django.shortcuts
    book = get_object_or_404(Book, slug=slug)

    return render(request, "book_store/book_detail.html", {
        "title": book.title,
        "rating": book.rating,
        "author": book.author,
        "is_bestseller": book.is_bestselling

    })
