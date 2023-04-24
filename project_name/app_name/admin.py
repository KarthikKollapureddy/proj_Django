from django.contrib import admin

# Register your models here.
from . import models

myModels = [models.User, models.MoM, models.feedback]  # iterable list
admin.site.register(myModels)
