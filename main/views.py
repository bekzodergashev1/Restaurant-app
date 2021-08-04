from audioop import reverse

from django.shortcuts import render, redirect
from django.utils.timezone import activate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from my_srartapp import settings
from .decorators import *
from .forms import *
from .models import *



@login_required(login_url='login')
@allowed_users(allowed_users=['admin', 'user', 'manager'])
def home(request, current_language=None):

    current_language == request.POST.get('lang')
    if current_language == settings.LANGUAGES[0][0]:
        reverse('pages/home')
        activate('en')
    elif current_language == settings.LANGUAGES[1][0]:
        reverse('pages/home')
        activate('uz')

    return render(request, 'pages/home.html')


@allowed_users(allowed_users=['admin', 'user', 'manager'])
def Menu(request, *args, **kwargs):
    menus = MenuItem.objects.all()
    categorys = Menu_category.objects.all()
    context = {'categorys': categorys, 'menus': menus}
    return render(request, 'pages/menu.html', context)


@allowed_users(allowed_users=['admin', 'user', 'manager'])
def Reservation(request):

    return render(request, 'pages/reservation.html')


@allowed_users(allowed_users=['admin', 'user', 'manager'])
def About(request):
    return render(request, 'pages/about.html')


@allowed_users(allowed_users=['admin', 'user', 'manager'])
def Contact_Us(request):
    form = ContactsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    form = ContactsForm()
    context = Contact_us.objects.all()

    return render(request, 'pages/contact_us.html', {'form': form, 'context': context})


@unauthenticated_user
def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Accound was created for' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'pages/register.html', context)


@unauthenticated_user
def Loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,
                                        password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'pages/login.html', context)


def Logoutuser(request):
    logout(request)
    return redirect('home')


def createMenuItem(request):
    form = MenuItemForm()
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')

    context = {'form': form}
    return render(request, 'pages/order_form.html', context)


def updateMenuItem(request, pk):
    order = MenuItem.objects.get(id=pk)
    form = MenuItemForm(instance=order)
    if request.method == "POST":
        form = MenuItemForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('menu')
    context = {'form': form}
    return render(request, 'pages/order_form.html', context)


def deleteMenuItem(request, pk):
    order = MenuItem.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("menu")
    return render(request, 'pages/delete.html', {'item':order})