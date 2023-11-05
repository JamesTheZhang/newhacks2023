from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import *
from .models import *

# Landing page
def landing_page(request):
    return render(request, "users/landing_page.html")

# Regsitration
def registration(request):
    # Submission of form
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, f"Account Sucessfully Created!")
            return redirect("login")
        
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'users/registration.html', {"form": registration_form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile Updated Successfully!")
            return redirect("profile")
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.userprofile)

    return render(request, 'users/profile.html', {"u_form": u_form, "p_form": p_form})

def map(request):
    return render(request, "users/map.html")

# View for sending Json data to react frontend
class UserDataView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
