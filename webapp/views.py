from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddTaskForm, UpdateTaskForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import task

#HomePage
def home(request):
    # return HttpResponse("Hello, world. You're at the webapp home.")
    return render(request, 'webapp/index.html')

#Register a User
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('my-login')
    context = {'form': form}
    return render(request, 'webapp/register.html', context)
    

# Login a User

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context=context) 

# Dashboard

@login_required(login_url='my-login')
def dashboard(request):
    
    my_tasks = task.objects.filter(user=request.user)
    context = {'tasks': my_tasks}
    return render(request, 'webapp/dashboard.html',context = context)



# Logout User

def user_logout(request):
    auth.logout(request)
    messages.success(request, 'Logout Successfully!')
    return redirect('my-login')

# Create a Task
@login_required(login_url='my-login')
def create_task(request):
    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            messages.success(request, 'Task Created!')
            return redirect('dashboard')
    else:
        form = AddTaskForm()
    context = {'form': form}
    return render(request, 'webapp/create-task.html', context)


# Update a Record
@login_required(login_url='my-login')
def update_task(request, pk):
    record = task.objects.get(id=pk, user=request.user)
    
    form = UpdateTaskForm(instance=record)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Updated!')
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/update-task.html', context)
    
# View a Record
@login_required(login_url='my-login')
def view_task(request, pk):
    all_task = task.objects.get(id=pk)
    context = {'task': all_task}
    return render(request, 'webapp/view-task.html', context)

# Delete a Record
from django.shortcuts import get_object_or_404

@login_required(login_url='my-login')
def delete_task(request, pk):
    task_to_delete = get_object_or_404(task, id=pk,user=request.user)  # Retrieve the task or raise a 404 if not found
    task_to_delete.delete()  # Delete the task
    messages.success(request, 'Task Deleted!')
    return redirect('dashboard')  # Redirect to the dashboard