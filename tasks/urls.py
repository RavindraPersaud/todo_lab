from django.urls import path
from . import views

# Namespace for this app, so templates use names like "tasks:task_list".
app_name = "tasks"

urlpatterns = [
    # /tasks/            -> list of all tasks
    path("", views.task_list, name="task_list"),
    # /tasks/3/          -> one task; <int:pk> passes the id to the view
    path("<int:pk>/", views.task_detail, name="task_detail"),
    # /tasks/new/        -> create form
    path("new/", views.task_create, name="task_create"),
    # /tasks/3/edit/     -> update form
    path("<int:pk>/edit/", views.task_update, name="task_update"),
    # /tasks/3/delete/   -> delete confirmation
    path("<int:pk>/delete/", views.task_delete, name="task_delete"),
]
