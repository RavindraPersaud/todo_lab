from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoForm
from .models import Todo


# READ: list every task.
def task_list(request):
    # ORM query, roughly SELECT * FROM tasks_todo ORDER BY ... (ordering comes from Meta).
    tasks = Todo.objects.all()
    # Pass the tasks to the template as "tasks".
    return render(request, "tasks/task_list.html", {"tasks": tasks})


# READ: show one task. pk comes from <int:pk> in the URL.
def task_detail(request, pk):
    # Returns the task, or an HTTP 404 page if no task has this id.
    task = get_object_or_404(Todo, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})


# CREATE: GET shows an empty form, POST validates and saves a new task.
def task_create(request):
    if request.method == "POST":
        # Bind the submitted data to the form.
        form = TodoForm(request.POST)
        if form.is_valid():
            # INSERT a new row and get back the saved Todo object.
            task = form.save()
            # Post/Redirect/Get: redirecting stops a page refresh from resubmitting the form.
            return redirect("tasks:task_detail", pk=task.pk)
    else:
        # GET request: empty form.
        form = TodoForm()
    # Reached on GET, or on POST when the form is invalid.
    # An invalid form keeps the user's input and its error messages.
    return render(request, "tasks/task_form.html", {"form": form, "page_title": "New task"})


# UPDATE: GET shows the form filled with current values, POST saves the changes.
def task_update(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        # instance=task binds the data to the existing row,
        # so save() runs an UPDATE instead of creating a duplicate.
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_detail", pk=task.pk)
    else:
        # GET request: prefill the form with the task's current values.
        form = TodoForm(instance=task)
    # "task" is passed so the template knows this is an edit (used by the Cancel link).
    return render(request, "tasks/task_form.html",
                  {"form": form, "task": task, "page_title": "Edit task"})


# DELETE: GET only shows a confirmation page, POST actually deletes.
def task_delete(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        # DELETE only this one row.
        task.delete()
        # Back to the list, since the detail page no longer exists.
        return redirect("tasks:task_list")
    # GET request: display the confirmation page without removing anything.
    return render(request, "tasks/task_confirm_delete.html", {"task": task})
