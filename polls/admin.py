from django.contrib import admin

# Register your models here.
from .models import TodoModel, Play

admin.site.register(TodoModel)
admin.site.register(Play)