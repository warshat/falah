from django.contrib import admin

# Register your models here.
from .models import User
from .models import Worker
from .models import Service



admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Service)