from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signing up
            return redirect("home")  # Redirect to home page
    else:
        form = UserCreationForm()

    return render(request, "core/signup.html", {"form": form})