from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


def index(req):
    return render(req, 'home/index.html')
