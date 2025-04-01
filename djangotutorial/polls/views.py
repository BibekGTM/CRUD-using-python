from django.shortcuts import render

def index(request):
    return HttpResponse("Hello Wrold!! You're at the polls index.")