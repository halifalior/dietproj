
from django.contrib.auth import login
from django.urls import reverse
from .forms import UserProfileForm , CustomUserCreationForm
from django.shortcuts import redirect, render

def buildmenu(profile,bmi,cal):
    return "this is your daily menu"
def home(request):
    return render(request, "home.html")

def edit_profile(request):

    if request.method == "GET":
        form = CustomUserCreationForm()
        profile_form = UserProfileForm()
        profile=profile_form.save(commit=False)
        context = {'form':form , 'profile_form':profile_form}
        return render(
            request, "profile.html",
            context
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
        return render(request, "home.html")
