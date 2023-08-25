# containt all url for challenges module

from django.urls import path
from . import views
# from the same folder imnport views.py


# mapping all routes for this module
urlpatterns = [
    path("", views.index),  # /bookstore/
    path("<slug:slug>", views.book_detail, name="book-detail")
]
