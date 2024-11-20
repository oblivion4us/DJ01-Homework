from django.http import HttpResponse

def index(responce):
    return HttpResponse("<h1>Привет!</h1>")

def data(responce):
    return HttpResponse("<h1>Страница data</h1>")

def test(responce):
    return HttpResponse("<h1>Страница test</h1>")