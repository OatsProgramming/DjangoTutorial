from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Create a function that represent the view

def index(response):
    return HttpResponse('<h1>Hello World</h1>') # You can change the text format to a header or a body or whatnot by giving it a HTML tag (e.g. <h1>"Enter text here"</h1>)

def v1(response):
    return HttpResponse('<h1>view 1</h1>')
