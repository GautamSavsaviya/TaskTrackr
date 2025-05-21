from django.shortcuts import render, HttpResponse, redirect
from todo.models import Todo
from todo.forms import TodoForm


# Create your views here.
def home(request):
    tasks = Todo.objects.all()
    form = TodoForm()

    context = {"tasks": tasks, "form": form}
    return render(request, "todo/index.html", context=context)


def filter(request):
    if request.method == "GET":
        filter = request.GET.get("status")

        tasks = Todo.objects.filter(status=filter)

        context = {"tasks": tasks, "filter": filter}
        return render(request, "todo/index.html", context=context)
    return redirect("home")
