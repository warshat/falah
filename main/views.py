from django.http import HttpResponse
from django.template import loader


def index(request):
    #  return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render())