"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # Django's built-in admin site, used only to inspect data.
    path("admin/", admin.site.urls),
    # Every URL starting with tasks/ is handled by tasks/urls.py.
    path("tasks/", include("tasks.urls")),
    # Visiting the site root (/) redirects to the task list.
    path("", RedirectView.as_view(pattern_name="tasks:task_list")),
]