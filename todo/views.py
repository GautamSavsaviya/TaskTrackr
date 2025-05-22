from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from todo.models import Todo
from todo.forms import AddTodoForm, UpdateTodoForm
from django.contrib import messages


# Create your views here.
def home(request):
    tasks = Todo.objects.all().order_by("due_date")
    form = AddTodoForm()
    update_forms = {task.id: UpdateTodoForm(instance=task) for task in tasks}
    context = {"tasks": tasks, "form": form, "update_forms": update_forms}
    return render(request, "todo/index.html", context=context)


def filter(request):
    if request.method == "GET":
        filter = request.GET.get("status")

        tasks = Todo.objects.filter(status=filter)

        context = {"tasks": tasks, "filter": filter}
        return render(request, "todo/index.html", context=context)
    return redirect("home")


def add_task(request):
    if request.method == "POST":
        form = AddTodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Added Successfully.")

    return redirect("home")


def update_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        form = UpdateTodoForm(request.POST, instance=task)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated Successfully.")

    return redirect("home")


def delete_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        task.delete()
        messages.success(request, f"Task `{task.title}` Deleted Successfully.")
    return redirect("home")
