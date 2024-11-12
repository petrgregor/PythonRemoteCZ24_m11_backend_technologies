from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # http://127.0.0.1:8000/hello/
    return HttpResponse('Hello, World!')


def hello2(request, word):
    # http://127.0.0.1:8000/hello2/nice/
    return HttpResponse(f'Hello, {word} world!')


def hello3(request):
    # http://127.0.0.1:8000/hello3?word=cruel
    word = request.GET.get('word', '')
    return HttpResponse(f'Hello, {word} world!')





def add(request, num1, num2):
    # http://127.0.0.1:8000/add/2/3/
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")


def add2(request):
    # http://127.0.0.1:8000/add2 -> 0 + 0 = 0
    # http://127.0.0.1:8000/add2?num1=2 -> 2 + 0 = 2
    # http://127.0.0.1:8000/add2?num1=2&num2=3 -> 2 + 3 = 5
    # http://127.0.0.1:8000/add2?num2=2&num1=3 -> 3 + 2 = 5
    num1 = int(request.GET.get('num1', 0))
    num2 = int(request.GET.get('num2', 0))
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")
