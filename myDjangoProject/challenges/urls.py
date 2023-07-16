# contant all url for challenges module

from django.urls import path

# from the same folder imnport views.py
from . import views

# mapping all routes for this module
urlpatterns = [
    path("january", views.index),
    path("february", views.february)
]
