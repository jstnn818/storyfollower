from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterUserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, ("There was an error logging in"))
            return redirect("members:login")
    else:
        return render(request, "authenticate/login.html", {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Logout successful"))
    return redirect("members:login")

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Sign Up Successful"))
            return redirect("home")
    else:
        form = RegisterUserForm()
            
    return render(request, "authenticate/register.html", {
        'form': form,
    })
    
def access_denied(request, owner_id):
    owner = User.objects.get(pk=owner_id)
    return render(request, "authenticate/access_denied.html", {
        'owner': owner,
    })