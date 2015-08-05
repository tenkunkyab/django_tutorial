from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango About says Hey there World!")

