from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book

# Create your views here.
def books(request):
    mybooks = Book.objects.all().values()
    template = loader.get_template('all_books.html')
    context = {
        'mybooks': mybooks,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    book = Book.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'book': book,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
      'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))