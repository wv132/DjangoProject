from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    tekst = "Hello, Wouter. You're at the polls index."
    return HttpResponse(tekst)

