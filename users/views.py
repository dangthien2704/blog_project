from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from users.forms import ProfileUpdateForm, UserForm, UserProfileForm, UserUpdateForm

def home(request):
    return render(request, "users/home.html")


@login_required
def profile(request):
    if request.method == "POST":
        user_uform = UserUpdateForm(request.POST, instance=request.user)
        profile_uform = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profileinfo
        )

        if user_uform.is_valid() and profile_uform.is_valid():
            user_uform.save()
            profile_uform.save()
            messages.success(request, "Your account has been updated successful!")

            return redirect("profile")

    else:
        user_uform = UserUpdateForm(instance=request.user)
        profile_uform = ProfileUpdateForm(instance=request.user.profileinfo)

    context = {"user_uform": user_uform, "profile_uform": profile_uform}
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    return render(request, "users/logout.html")


def register(request):
    form = UserForm()
    profile = UserProfileForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        profile = UserProfileForm(request.POST)

        if form.is_valid() and profile.is_valid():

            user_request = (
                form.save()
            )  # when we using form.save() it means we creating a user
            profile_request = profile.save(
                commit=False
            )  # Now we creating a new form but
            # we dont want to save profile to
            # database right away. We will after we've
            # done with creating a relation between user
            # and profile so we use commit=False
            profile_request.user = user_request
            profile_request.save()

            messages.success(request, "Your account has been created!")

            return redirect("home")

    else:
        form = UserForm()
        profile = UserProfileForm()
    return render(request, "users/register.html", {"form": form, "profile": profile})
