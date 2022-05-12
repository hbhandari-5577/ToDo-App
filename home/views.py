from django.shortcuts import render
from home.models import Task

# Create your views here.
def home(request):
    context = {"success": False, "name": "Zemu"}
    if request.method == "POST":
        # Handle the form
        title = request.POST["title"]
        desc = request.POST["desc"]
        ins = Task(task_title = title, task_desc = desc)
        ins.save()
        context = {"success": True}
    return render(request, "index.html", context)

def tasks(request):
    all_tasks = Task.objects.all()
    context = {"tasks": all_tasks}
    return render(request, "tasks.html", context)
