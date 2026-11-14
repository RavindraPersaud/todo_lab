from django.contrib import admin
from .models import Todo

# Makes Todo visible in /admin/ for inspecting data.
# The CRUD workflow itself is done through the app's own pages.
admin.site.register(Todo)
