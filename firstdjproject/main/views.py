from django.http import HttpResponse

def index(responce):
    return HttpResponse("<h1>Привет!</h1>")

