from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm, AddTaskForm, UpdateTaskForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record

# Home
def home(request):
    return render(request, 'webapp/index.html')

# Register
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    
    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)

# Login
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
        
    context = {'form':form}
    return render(request, 'webapp/login.html', context=context)

# Logout
def logout(request):
    auth.logout(request)
    return redirect("login")

# Dashboard
@login_required(login_url='login')
def dashboard(request):
    rec = Record.objects.all()
    context = {'records':rec}
    return render(request, 'webapp/dashboard.html', context=context)

#Create task
@login_required(login_url='login')
def create(request):
    form = AddTaskForm()

    if request.method == "POST":
        form = AddTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
    
    context = {'form':form}
    return render(request, 'webapp/create-record.html', context=context)

# update task
@login_required(login_url='login')
def update(request, pk):
    rec = Record.objects.get(id = pk)
    form = UpdateTaskForm(instance=rec)

    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=rec)

        if form.is_valid():
            form.save()

            return redirect("dashboard")
    
    context = {'form':form}
    return render(request, 'webapp/update-record.html', context=context)

# view task
@login_required(login_url='login')
def view(request, pk):
    all_task = Record.objects.get(id = pk)
    context = {'task':all_task}
    return render(request, 'webapp/view-record.html', context=context)

# delete
@login_required(login_url='login')
def delete(request, pk):
    rec = Record.objects.get(id = pk)
    rec.delete()
    return redirect('dashboard')