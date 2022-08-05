from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import UserInfo


def user_form(request):
    context = dict()
    # userdata = {
    #     'username': request.session['username'],
    #     'logged_in': request.session['logged_in'],
    # }
    # context['data'] = userdata
    if request.method == "POST":
        UserInfo.objects.create(name=request.POST['name'],
                                email=request.POST['email'],
                                phone=request.POST['phone'])
        messages.success(request, 'Data Successfully Inserted')
        return redirect("/")
    return render(request, 'info/home.html', context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = UserCreationForm()
    return render(request, 'info/register.html', {"form": form})


@login_required()
def app_list(request):
    context = dict()
    context['app_list'] = UserInfo.objects.all()
    return render(request, 'info/app_list.html', context)
