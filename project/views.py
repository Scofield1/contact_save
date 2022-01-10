from django.shortcuts import render, redirect
from .forms import ContactForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Contact


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {})


@login_required(login_url='login')
def create(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Saved Successfully!')
            return redirect('create')
    context = {'form': form}
    return render(request, 'create.html', context)


@login_required(login_url='login')
def update(request, pk):
    model = Contact.objects.get(id=pk)
    form = ContactForm(request.POST or None, instance=model)
    if form.is_valid():
        form.save()
        messages.success(request, 'Changed made')
        return redirect('list')
    else:
        forms = ContactForm()
    context = {'form': form}
    return render(request, 'update.html', context)


@login_required(login_url='login')
def contact_list(request):
    model = Contact.objects.all()
    context = {'models': model}
    return render(request, 'list.html', context)


@login_required(login_url='login')
def delete(request, pk):
    model = Contact.objects.get(id=pk)
    if request.method == 'POST':
        model.delete()
        return redirect('list')
    return render(request, 'delete.html', {})


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
        else:
            forms = CreateUserForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password not is Incorrect')
    return render(request, 'login.html', {})


def log_out(request):
    logout(request)
    return redirect('/')

