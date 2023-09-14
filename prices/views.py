from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    return HttpResponse("Fill home page!")


def about(request):
    return HttpResponse("Fill about page!")


def contact(request):
    return HttpResponse("Fill contact page!")
