from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.forms import UserLoginform, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == "POST":
        form = UserLoginform(data= request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username= username, password= password)
            if user:
                auth.login(request, user)
                messages.success(request=request, message=f"Welcome {username}!!!")
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginform()

    context = {
        "title": "Home - authorization",
        "form": form,
    }
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data= request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request= request, message= f"{user.username} was register successfully")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {
        "title": "Home - registration",
        "form": form,
    }
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    
    if request.method == 'POST':
        form = ProfileForm(data= request.POST, instance= request.user, files= request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request= request, message="Profile succesfully update")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance= request.user)

    context = {
        "title": "Home - profile",
        "form": form,
    }
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    messages.success(request= request, message= f"{request.user.username} is logout")
    auth.logout(request)
    return redirect(reverse("main:index"))
