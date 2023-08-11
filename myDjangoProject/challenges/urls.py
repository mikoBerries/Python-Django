# containt all url for challenges module

from django.urls import path

# from the same folder imnport views.py
from . import views

# mapping all routes for this module
urlpatterns = [
    path("", views.index, name="index"),  # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
