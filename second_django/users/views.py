from django.shortcuts import render, redirect
from .forms import (CustomUserCreationForm, EditProfileInfo,
                    CustomUserChangeForm, CustomPasswordChangeForm,
                    PostContactForm, )
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import PasswordChangeForm
from .models import SignUpAccess, User, UserProfile
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'users/home.html', {})


def register_user(request):
    user = User
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            registration_token = form.cleaned_data['reg_number']
            SignUpAccess.objects.filter(
                reg_key=registration_token).update(is_used=True)
            SignUpAccess.objects.filter(
                reg_key=registration_token).update(user_email=email)
            SignUpAccess.objects.filter(reg_key=registration_token).update(
                user_first_name=first_name)
            SignUpAccess.objects.filter(reg_key=registration_token).update(
                user_last_name=last_name)
            messages.success(request, 'You Have Registered...')
            return redirect('home')

    else:
        form = CustomUserCreationForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'users/login.html', {})


def edit_user_info(request):
    user = User
    if request.method == 'POST':
        form = EditProfileInfo(
            request.POST, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProfileInfo(instance=request.user.user_profile)

    context = {'form': form}

    return render(request, 'users/edit_profile.html', context)


def change_user_info(request):
    user = User
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {'form': form}

    return render(request, 'users/edit_detail.html', context)


def combined_edit(request):
    user = User
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        formed = EditProfileInfo(
            request.POST, instance=request.user.user_profile)
        former = CustomPasswordChangeForm(data=request.POST, user=request.user)
        old_password = former.data['old_password']
        new_password1 = former.data['new_password1']
        new_password2 = former.data['new_password2']
        if form.is_valid():
            form.save()
        if formed.is_valid():
            formed.save()
        if former.is_valid():
            former.save()
        if len(old_password) == 0 or len(new_password1) == 0 or len(new_password2) == 0:
            return redirect('home')
        if form.is_valid() and formed.is_valid() and former.is_valid():
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
        formed = EditProfileInfo(instance=request.user.user_profile)
        former = CustomPasswordChangeForm(user=request.user)

    context = {'form': form, 'formed': formed, 'former': former}

    return render(request, 'users/combined_edit.html', context)


def contact_form(request):
    if request.method == 'POST':
        form = PostContactForm(request.POST)
        if form.is_valid():
            form.save()
            sender_email = form.data['sender_email']
            full_name = form.data['sender_full_name']
            message = form.data['message']

            context = {
                'sender_email': sender_email,
                'full_name': full_name,
                'message': message,
                'filled': True,
            }
            return render(request, 'users/contact.html', context)
    else:
        form = PostContactForm()

    context = {'form': form}

    return render(request, 'users/contact.html', context)
