from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "core/home.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home after login
    else:
        form = AuthenticationForm()

    return render(request, "core/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to login after logout

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signup
            return redirect("home")  # Redirect to home after signup
    else:
        form = UserCreationForm()

    return render(request, "core/signup.html", {"form": form})