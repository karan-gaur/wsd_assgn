from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Hello, Django! My name is Karan from IS-601 Class")

def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(request, "hello/hello_there.html", {
        'name': name,
        'date': datetime.now()
    })