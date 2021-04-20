from django.shortcuts import render, redirect, resolve_url, Http404
from django.contrib.auth.decorators import login_required
from .forms import ToDoListForm
from .models import ToDoList

def check_author(request, task):
    """Check are author of task is user or not"""
    if request.user != task.author:
        raise Http404
    return True
    

def home(request):
    """Home function that make CRUD tasks"""

    form = ToDoListForm()

    # if task_id exists mean it will be update not create
    task_id = request.GET.get('task_id')
    if task_id:
        task = ToDoList.objects.get(id=task_id)

        #Raise 404 page if autor not cuerrent user |
        check_author(request, task)
        form = ToDoListForm(instance=task)
    
    if request.method == 'POST':
        task_id_post_method = request.POST.get('task_id')
        if 'plus' in request.POST:
            form = ToDoListForm(request.POST)
            # Update Taske
            if task_id:
                task = ToDoList.objects.get(id=task_id)
                
                check_author(request, task)
                form = ToDoListForm(request.POST, instance=task)

            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.author = request.user
                new_form.save()
        
        elif 'delete' in request.POST:
            task = ToDoList.objects.get(id=task_id_post_method)

            #Raise 404 page if autor not cuerrent user
            check_author(request, task)
            task.delete()

        elif 'update' in request.POST:
            return redirect(resolve_url(f'/?task_id={task_id_post_method}'))

        elif 'finsh' in request.POST:
            task = ToDoList.objects.get(id=task_id_post_method)
            
            #Raise 404 page if autor not cuerrent user
            check_author(request, task)

            if task.completed:
                task.completed = False
            else:
                task.completed = True
            
            task.save()

        return redirect('/')

    tasks = ToDoList.objects.filter(author=request.user)
    tasks_completed = tasks.filter(completed=True)

    context = {
        'form':form,
        'tasks':tasks,
        'tasks_completed':tasks_completed,
    }
    return render(request, 'todo/index.html', context)






