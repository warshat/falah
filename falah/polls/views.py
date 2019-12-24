from django.http import HttpResponse


def index(req):
    print(req)
    return HttpResponse("Hello, world. You're at the polls index.")
