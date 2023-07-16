from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    """for index pages"""
    return HttpResponse("This is index ")


def february(request):
    """for febuary """
    return HttpResponse("This is february ")
