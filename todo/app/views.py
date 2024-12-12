from django.shortcuts import render,get_object_or_404
from .models import List,Task
from django.contrib.auth.decorators import login_required

from .forms import ListForm,TaskForm

@login_required(login_url='/auth/login/')
def show_lists(request):
    
    if request.method == "POST":
        form = ListForm(request.POST) 
        if form.is_valid():
            if 'Delete' in request.POST:
                List.objects.filter(**form.cleaned_data).delete()
            else:
                List.objects.create(**form.cleaned_data)
    
    lists = List.objects.filter(user = request.user)
    
    context = {
        'lists':lists
    }
    return render(request,'lists.html',context)


@login_required(login_url='/auth/login/')
def list_details(request,list_id):

    list = get_object_or_404(List,id = list_id,user = request.user)
    tasks = Task.objects.filter(list = list)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task_name = form.cleaned_data['name']
            if "delete" in request.POST:
                Task.objects.filter(name = task_name).delete()
            elif "create" in request.POST:
                form.save()

        if "update" in request.POST:
            for task in tasks:
                if f"task_id_{task.id}" in request.POST:
                    task.status = True
                else:
                    task.status = False
                task.save()

    context = {
        'list':list,
        'tasks':tasks
    }

    return render(request,'tasks.html',context)

def main(request):
    return render(request,'main.html')

