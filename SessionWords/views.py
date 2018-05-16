from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse("To run the app use the link: <a href='/session_words'>Session Words</a>")