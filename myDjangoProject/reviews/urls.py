from django.urls import path

from . import views

urlpatterns = [
    # path("", views.review),
    # calling view using inherited django.View class
    path("", views.ReviewView.as_view()),
    path("thank-you", views.thank_you)
]
